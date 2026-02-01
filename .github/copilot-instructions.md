# Copilot / AI Agent Instructions for techaiforengineer ⚡️

## Purpose
This repository is a small demo/workshop project that prints a message and demonstrates basic ML imports (`pandas`, `scikit-learn`, `matplotlib`). The README contains Codespaces setup steps. Keep changes minimal, self-contained, and easy to run in Codespaces.

## Quick facts (What an agent needs to know)
- Entry point: `main.py` (very small script). Example output: `Hello from GitHub Codespaces!` and a confirmation of ML libraries.
- Dependencies: listed in `requirements.txt` (`pandas`, `scikit-learn`, `matplotlib`).
- README includes a short Codespaces quickstart: open the repo > Codespaces tab > Create codespace on `main`.

## When making changes
- Keep the demo lightweight and easy to run in Codespaces.
- If you add or change Python dependencies, update `requirements.txt` (top-level) and include install instructions in README.
- If you add executable scripts, include clear usage examples in README and keep output deterministic for demo/tests.

## Build / Run / Debug (explicit commands)
- Install deps: `python3 -m pip install -r requirements.txt`
- Run the demo: `python3 main.py` (expected short stdout message)
- Run with debugger: `python3 -m pdb main.py` or use VS Code Codespaces debugger configuration

## Tests & CI
- There is no test suite currently. If you add tests:
  - Use `pytest` and add it to `requirements.txt` or a `pyproject`/`dev` requirements file.
  - Place tests under `tests/` and use the `test_*.py` naming convention.
  - Keep tests fast and deterministic to be Codespaces/CI-friendly.

## Coding patterns & conventions observed
- This repository favors minimal, explicit examples (single-file demo). Avoid introducing heavy frameworks or complex CI unless the change justifies it.
- Documentation-first: small README exists; ensure any behavior changes are reflected in README.

## PR & review expectations
- Small, focused PRs with short descriptions of the intent and impact.
- Mention changes to `requirements.txt` or README in the PR description.

## Integration points / external dependencies
- Python packages from PyPI only (declared in `requirements.txt`). No other external services or APIs are present.

## Examples for agents (do this, not that)
- Do: Add a small, self-contained example or notebook that shows how to use the listed libraries. Include clear run steps in README.
- Do: Update `requirements.txt` when adding dependencies and show the commands to install them.
- Don’t: Add long-running background services or infrastructure code that complicates quick Codespaces runs.

---

If anything in this doc is unclear or you want more detail (tests, CI suggestions, or a sample notebook), tell me which section to expand and I’ll iterate. ✅