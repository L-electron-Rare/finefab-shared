# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

finefab-shared contains JSON Schema contracts — single source of truth for data types shared between life-core (Python) and life-reborn (TypeScript).

## Commands

```bash
python scripts/generate_types.py   # validate schemas + regenerate types
```

## Architecture

`schemas/*.json` are the source of truth. `python/` and `typescript/` are generated — never hand-edit. Run `generate_types.py` after any schema change.
