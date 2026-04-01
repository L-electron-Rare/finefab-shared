# finefab-shared

Shared contracts and types for the FineFab ecosystem -- JSON Schema, Pydantic models, and TypeScript types.

Part of the [FineFab](https://github.com/L-electron-Rare) platform.

## What it does

- Centralizes JSON Schema definitions used across all FineFab repos
- Exposes aligned Python (Pydantic) models and TypeScript types from a single source
- Validates inter-service contracts at CI time
- Enables spec-first development: schema changes propagate to all consumers

## Tech stack

Python 3.12+ / TypeScript / JSON Schema

## Quick start

```bash
# Python
python -m venv .venv && source .venv/bin/activate
pip install -e .

# Generate types from schemas
python scripts/generate_types.py
```

## Project structure

```
schemas/      # JSON Schema contract definitions
python/       # Pydantic models and utilities
typescript/   # TypeScript types and utilities
scripts/      # Type generation and validation
```

## Related repos

| Repo | Role |
|------|------|
| [life-core](https://github.com/L-electron-Rare/life-core) | AI backend engine |
| [life-reborn](https://github.com/L-electron-Rare/life-reborn) | API gateway |
| [life-web](https://github.com/L-electron-Rare/life-web) | Operator cockpit UI |
| [life-spec](https://github.com/L-electron-Rare/life-spec) | Functional specifications and BMAD gates |

## License

[MIT](LICENSE)
