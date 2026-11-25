# `jezz-template-python` — JBC Edition 1.3 Starter

Turnkey **Python 3.14+** starter repository governed by the **Jezz Software Building Code (`JBC` Edition 1.3)** and **Permit-and-Contract Engineering (`PCE`)**.

## Architectural Layout (`domain` + `gateway`)

- **`src/ledger_starter/domain/`** — Pure conserved settlement fee calculus with closed Pydantic models (`extra="forbid"`, `frozen=True`, `strict=True`, `allow_inf_nan=False`), `@validate_call` runtime circuit breakers, and Z3-discharged `@icontract` preconditions/postconditions.
- **`src/ledger_starter/gateway/`** — Untrusted JSON wire ingress adapter routing exclusively through `ledger_starter.domain`'s perimeter barrel exports.
- **`blueprint.json`** — Sealed architectural netlist (`BlueprintGraph`) enforced against `SHORT_CIRCUIT` and `ENCAPSULATION_BREACH` defects via Layout-vs-Schematic (`LVS`).
- **`tests/test_settlement.py`** — Universally quantified `Hypothesis` conservation property suite and schema rejection falsifiers.

## Quickstart

Scaffold locally via `jezz` or click **Use this template** on GitHub:

```bash
uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz init my-service --scaffold python
cd my-service
uv sync --all-groups
```

## Verification Gates

```bash
# 1. Native static & property-based gates
uv run ruff check .
uv run mypy .
uv run pytest

# 2. Statutory JBC Edition 1.3 inspection (30 static provisions)
uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz inspect .

# 3. Deductive Z3 SMT contract proof discharge
uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz prove . --require-deductive

# 4. Layout-vs-Schematic (LVS) architectural verification & interactive CAD Sheet A-1 / E-1
uvx --from git+https://github.com/futileandstupid/jezz@v0.6.0 jezz blueprint . --verify-target blueprint.json --write-html blueprint.html
```
