#!/usr/bin/env python3
"""Generate Pydantic v2 models and TypeScript interfaces from JSON schemas."""

import json
import keyword
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


def sanitize_python_identifier(name: str) -> str:
    """Convert a schema property name to a valid Python field name."""
    sanitized = name.replace("-", "_").replace(".", "_")
    sanitized = re.sub(r"\W", "_", sanitized)
    if not sanitized:
        sanitized = "field"
    if sanitized[0].isdigit():
        sanitized = f"field_{sanitized}"
    if keyword.iskeyword(sanitized):
        sanitized = f"{sanitized}_"
    return sanitized


def json_type_to_python(
    prop: dict,
    *,
    parent_name: str,
    prop_name: str,
    nested_models: list[str],
    emitted_nested_models: set[str],
) -> str:
    """Map JSON Schema type to Python type annotation."""
    t = prop.get("type", "Any")
    if isinstance(t, list):
        # Handle nullable types like ["string", "null"]
        types = [
            json_type_to_python(
                {**prop, "type": x},
                parent_name=parent_name,
                prop_name=prop_name,
                nested_models=nested_models,
                emitted_nested_models=emitted_nested_models,
            )
            for x in t
            if x != "null"
        ]
        base = types[0] if types else "Any"
        if "null" in t:
            return f"{base} | None"
        return base

    if t == "array" and "items" in prop:
        item_type = json_type_to_python(
            prop["items"],
            parent_name=parent_name,
            prop_name=f"{prop_name}_item",
            nested_models=nested_models,
            emitted_nested_models=emitted_nested_models,
        )
        return f"list[{item_type}]"

    if t == "object" and prop.get("properties"):
        nested_name = f"{parent_name}{sanitize_name(prop_name)}"
        if nested_name not in emitted_nested_models:
            emitted_nested_models.add(nested_name)
            nested_models.extend(
                generate_pydantic_model_parts(
                    prop,
                    nested_name,
                    emitted_nested_models=emitted_nested_models,
                )
            )
        return nested_name

    mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict[str, Any]",
        "array": "list[Any]",
        "null": "None",
    }

    return mapping.get(t, "Any")


def format_ts_property(name: str, ts_type: str, optional: bool, indent: int) -> list[str]:
    """Render a TypeScript property, including multiline inline object types."""
    prefix = "  " * indent + f"{name}{'?' if optional else ''}: "

    if "\n" not in ts_type:
        return [f"{prefix}{ts_type};"]

    lines = ts_type.splitlines()
    lines[0] = prefix + lines[0]
    lines[-1] = lines[-1] + ";"
    return lines


def json_type_to_ts(prop: dict, *, indent: int = 0) -> str:
    """Map JSON Schema type to TypeScript type."""
    t = prop.get("type", "unknown")
    if isinstance(t, list):
        types = [json_type_to_ts({**prop, "type": x}, indent=indent) for x in t]
        return " | ".join(types)

    if t == "array" and "items" in prop:
        item_type = json_type_to_ts(prop["items"], indent=indent)
        return f"{item_type}[]"

    if t == "object" and prop.get("properties"):
        lines = ["{"]
        required = set(prop.get("required", []))
        for prop_name, prop_schema in prop["properties"].items():
            lines.extend(
                format_ts_property(
                    prop_name,
                    json_type_to_ts(prop_schema, indent=indent + 1),
                    optional=prop_name not in required,
                    indent=indent + 1,
                )
            )
        lines.append(f"{'  ' * indent}}}")
        return "\n".join(lines)

    mapping = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "object": "Record<string, unknown>",
        "array": "unknown[]",
        "null": "null",
    }

    return mapping.get(t, "unknown")


def generate_pydantic_model_parts(
    schema: dict,
    class_name: str,
    *,
    emitted_nested_models: set[str],
) -> list[str]:
    """Generate a Pydantic v2 model from a JSON Schema."""
    lines = []
    nested_models: list[str] = []

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
        return ["\n".join(lines)]

    lines.append("    model_config = ConfigDict(extra='allow')")
    lines.append("")

    for prop_name, prop_schema in props.items():
        py_type = json_type_to_python(
            prop_schema,
            parent_name=class_name,
            prop_name=prop_name,
            nested_models=nested_models,
            emitted_nested_models=emitted_nested_models,
        )
        field_name = sanitize_python_identifier(prop_name)
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
    return nested_models + ["\n".join(lines)]


def generate_pydantic_model(schema: dict, class_name: str) -> str:
    """Generate a Pydantic v2 model from a JSON Schema."""
    return "\n\n".join(
        generate_pydantic_model_parts(
            schema,
            class_name,
            emitted_nested_models=set(),
        )
    )


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
        ts_type = json_type_to_ts(prop_schema, indent=1)
        desc = prop_schema.get("description", "")
        if desc:
            lines.append(f"  /** {desc} */")
        lines.extend(
            format_ts_property(
                prop_name,
                ts_type,
                optional=prop_name not in required,
                indent=1,
            )
        )

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
