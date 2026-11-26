# Project Instructions — JBC Edition 1.3 Python Workspace

## Methodology & Architecture
- Govern engineering work via **Permit-and-Contract Engineering (`PCE`)** and **Jezz Software Building Code (`JBC` Edition 1.3)**. Never frame deliverables around Agile user stories (`As a ..., I want ...`), "SDD", or Markdown task checklists (`- [ ]`).
- Maintain strict compartment isolation enforced by [`blueprint.json`](blueprint.json) Layout-vs-Schematic (`LVS`):
  - **`src/<pkg>/domain/`** — Pure domain logic, closed Pydantic models (`STRICT_FROZEN_CONFIG`: `extra="forbid"`, `frozen=True`, `strict=True`, `allow_inf_nan=False`), `@validate_call` / `@jezz_callable` runtime circuit breakers, and Z3-provable `@icontract` preconditions/postconditions.
  - **`src/<pkg>/gateway/`** — Untrusted I/O and wire boundary adapters routing strictly through `domain`'s public `__init__.py` barrel exports.
- Never hardcode host filesystem paths (`JBC-SEC-006`). Compute paths dynamically via `Path(__file__).resolve()`, `importlib.resources`, `tmp_path`, or `ContainedPath.from_parts(...)`.

## Statutory Verification Commands
- **Native Lint, Strict Types, & Hypothesis Suite:**
  `uv run ruff check . && uv run mypy . && uv run pytest`
- **JBC Edition 1.3 Static Inspection:**
  `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.1 jezz inspect .`
- **Z3 Deductive Contract Proof Discharge:**
  `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.1 jezz prove . --require-deductive`
- **Blueprint CAD & LVS Equivalence Gate (Refresh `blueprint.json` When Modifying Boundaries):**
  `uvx --from git+https://github.com/futileandstupid/jezz@v0.6.1 jezz blueprint . --verify-target blueprint.json`
