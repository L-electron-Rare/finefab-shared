#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
PY_OUT = ROOT / "python" / "finefab_shared" / "models" / "__init__.py"
TS_OUT = ROOT / "typescript" / "src" / "types" / "index.ts"

schemas = sorted(SCHEMAS_DIR.glob("*.json"))
if not schemas:
    raise SystemExit("No schema files found")


def to_pascal_case(stem: str) -> str:
    # Keep only alphanumeric separators, then PascalCase each chunk.
    normalized = re.sub(r"[^0-9a-zA-Z]+", "_", stem)
    parts = [part for part in normalized.strip("_").split("_") if part]
    if not parts:
        return "SchemaModel"
    name = "".join(part[:1].upper() + part[1:] for part in parts)
    # Python and TypeScript identifiers cannot start with a digit.
    if name[0].isdigit():
        return f"Schema{name}"
    return name

for schema in schemas:
    with schema.open("r", encoding="utf-8") as fh:
        json.load(fh)

py_lines = [
    '"""Auto-generated placeholder models from JSON schemas."""',
    "",
]
for schema in schemas:
    class_name = to_pascal_case(schema.stem)
    py_lines.append(f"class {class_name}:")
    py_lines.append(f'    """Derived from {schema.name}."""')
    py_lines.append(f'    schema_file: str = "{schema.name}"')
    py_lines.append("")

PY_OUT.write_text("\n".join(py_lines).rstrip() + "\n", encoding="utf-8")

ts_lines = [
    "// Auto-generated placeholder types from JSON schemas.",
    "",
]
for schema in schemas:
    type_name = to_pascal_case(schema.stem)
    ts_lines.append(f"export type {type_name} = Record<string, unknown>; // {schema.name}")

TS_OUT.write_text("\n".join(ts_lines).rstrip() + "\n", encoding="utf-8")

print(f"Validated {len(schemas)} schemas")
print(f"Wrote {PY_OUT.relative_to(ROOT)}")
print(f"Wrote {TS_OUT.relative_to(ROOT)}")
