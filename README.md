# finefab-shared

Bibliotheque de contrats et types partages pour l'ecosysteme FineFab.

## Role
- Centraliser les schemas JSON de reference.
- Exposer des modeles Python (Pydantic) et des types TypeScript alignes.
- Stabiliser les interfaces inter-repos (spec-first).

## Stack
- Python 3.12+
- TypeScript
- JSON Schema

## Structure cible
- `schemas/`: contrats JSON Schema
- `python/`: modeles et utilitaires Python
- `typescript/`: types et utilitaires TypeScript
- `scripts/`: generation/validation de types

## Demarrage rapide
```bash
# Python
python -m venv .venv && source .venv/bin/activate
pip install -e .

# Validation schemas (exemple)
python scripts/generate_types.py
```

## Roadmap immediate
- Finaliser la migration des contrats depuis `Kill_LIFE/specs/contracts`.
- Ajouter CI de validation schema + generation types.
- Verrouiller versionnement semantique des contrats.
