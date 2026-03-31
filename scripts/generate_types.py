#!/usr/bin/env python3
"""Generate Pydantic v2 models and TypeScript interfaces from JSON schemas."""

import json
import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).parent.parent / "schemas"
PYTHON_OUT = Path(__file__).parent.parent / "python" / "finefab_shared" / "models"
TS_OUT = Path(__file__).parent.parent / "typescript" / "src" / "types"


def sanitize_name(name: str) -> str:
    """Convert filename to PascalCase class name."""
    # Remove .schema.json or .json extension
    name = re.sub(r"\.schema\.json$|\.json$", "", name)
    # Convert to PascalCase
    parts = re.split(r"[_\-.]", name)
    return "".join(p.capitalize() for p in parts if p)


def json_type_to_python(prop: dict) -> str:
    """Map JSON Schema type to Python type annotation."""
    t = prop.get("type", "Any")
    if isinstance(t, list):
        # Handle nullable types like ["string", "null"]
        types = [json_type_to_python({"type": x}) for x in t if x != "null"]
        base = types[0] if types else "Any"
        if "null" in t:
            return f"{base} | None"
        return base

    mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict[str, Any]",
        "array": "list[Any]",
        "null": "None",
    }

    if t == "array" and "items" in prop:
        item_type = json_type_to_python(prop["items"])
        return f"list[{item_type}]"

    return mapping.get(t, "Any")


def json_type_to_ts(prop: dict) -> str:
    """Map JSON Schema type to TypeScript type."""
    t = prop.get("type", "unknown")
    if isinstance(t, list):
        types = [json_type_to_ts({"type": x}) for x in t]
        return " | ".join(types)

    mapping = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "object": "Record<string, unknown>",
        "array": "unknown[]",
        "null": "null",
    }

    if t == "array" and "items" in prop:
        item_type = json_type_to_ts(prop["items"])
        return f"{item_type}[]"

    return mapping.get(t, "unknown")


def generate_pydantic_model(schema: dict, class_name: str) -> str:
    """Generate a Pydantic v2 model from a JSON Schema."""
    lines = []

    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    description = schema.get("description", "") or schema.get("title", "")

    lines.append(f"class {class_name}(BaseModel):")
    if description:
        lines.append(f'    """{description}"""')
    lines.append("")

    if not props:
        lines.append("    model_config = ConfigDict(extra='allow')")
        lines.append("")
        return "\n".join(lines)

    lines.append("    model_config = ConfigDict(extra='allow')")
    lines.append("")

    for prop_name, prop_schema in props.items():
        py_type = json_type_to_python(prop_schema)
        field_name = prop_name.replace("-", "_").replace(".", "_")
        prop_desc = prop_schema.get("description", "")

        if prop_name in required:
            if prop_desc:
                lines.append(
                    f'    {field_name}: {py_type} = Field(..., alias="{prop_name}", description="{prop_desc}")'
                )
            elif field_name != prop_name:
                lines.append(
                    f'    {field_name}: {py_type} = Field(..., alias="{prop_name}")'
                )
            else:
                lines.append(f"    {field_name}: {py_type}")
        else:
            if "| None" not in py_type and py_type != "None":
                py_type = f"{py_type} | None"
            if field_name != prop_name:
                lines.append(
                    f'    {field_name}: {py_type} = Field(default=None, alias="{prop_name}")'
                )
            else:
                lines.append(f"    {field_name}: {py_type} = None")

    lines.append("")
    return "\n".join(lines)


def generate_ts_interface(schema: dict, name: str) -> str:
    """Generate a TypeScript interface from a JSON Schema."""
    lines = []
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    description = schema.get("description", "") or schema.get("title", "")

    if description:
        lines.append(f"/** {description} */")
    lines.append(f"export interface {name} {{")

    for prop_name, prop_schema in props.items():
        ts_type = json_type_to_ts(prop_schema)
        optional = "" if prop_name in required else "?"
        desc = prop_schema.get("description", "")
        if desc:
            lines.append(f"  /** {desc} */")
        lines.append(f"  {prop_name}{optional}: {ts_type};")

    if not props:
        lines.append("  [key: string]: unknown;")

    lines.append("}")
    return "\n".join(lines)


def main():
    schemas = sorted(SCHEMAS_DIR.glob("*.json"))

    if not schemas:
        print("No schemas found!", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(schemas)} schemas")

    # Ensure output dirs
    PYTHON_OUT.mkdir(parents=True, exist_ok=True)
    TS_OUT.mkdir(parents=True, exist_ok=True)

    # Ensure parent package init
    (PYTHON_OUT.parent / "__init__.py").touch()

    py_imports = []
    py_models = []
    ts_interfaces = []
    skipped = []

    for schema_path in schemas:
        try:
            with open(schema_path) as f:
                schema = json.load(f)
        except json.JSONDecodeError as e:
            print(f"  SKIP {schema_path.name}: invalid JSON ({e})")
            skipped.append(schema_path.name)
            continue

        class_name = sanitize_name(schema_path.name)
        print(f"  {schema_path.name} -> {class_name}")

        # Python
        model_code = generate_pydantic_model(schema, class_name)
        py_models.append(model_code)
        py_imports.append(class_name)

        # TypeScript
        ts_code = generate_ts_interface(schema, class_name)
        ts_interfaces.append(ts_code)

    # Write Python models
    py_header = '''"""Auto-generated Pydantic v2 models from finefab-shared schemas.

DO NOT EDIT — regenerate with: python scripts/generate_types.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

'''

    py_content = py_header + "\n\n".join(py_models)

    # Write __all__
    py_content += "\n\n__all__ = [\n"
    for name in py_imports:
        py_content += f'    "{name}",\n'
    py_content += "]\n"

    (PYTHON_OUT / "__init__.py").write_text(py_content)
    print(f"\nGenerated {len(py_imports)} Python models -> {PYTHON_OUT / '__init__.py'}")

    # Write TypeScript
    ts_header = """// Auto-generated TypeScript interfaces from finefab-shared schemas.
// DO NOT EDIT — regenerate with: python scripts/generate_types.py

"""
    ts_content = ts_header + "\n\n".join(ts_interfaces) + "\n"
    (TS_OUT / "index.ts").write_text(ts_content)
    print(f"Generated {len(ts_interfaces)} TypeScript interfaces -> {TS_OUT / 'index.ts'}")

    if skipped:
        print(f"\nSkipped {len(skipped)} schemas due to errors: {skipped}")

    print(f"\nDone: {len(py_imports)} models generated from {len(schemas)} schemas")


if __name__ == "__main__":
    main()
