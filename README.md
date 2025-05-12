# 🚀 Critical Traceable Calculator Project

This repository demonstrates **end-to-end traceability enforcement**. The design ensures that **only specified functionality** is implemented, and that **every requirement is tested** and **verified via CI**.

## ✅ Traceability Workflow

1. **Define Specification** → `SPECIFICATION.md`
2. **Define Requirements** → `docs/requirements.md` (with REQ-IDs)
3. **Implement Functions** → `src/calculator.py` (each function tied to REQ-ID)
4. **Test Functions** → `tests/` (each test tied to REQ-ID)
5. **Traceability Matrix** → Auto-generated via `GENERATE_TRACEABILITY_MATRIX.py`
6. **CI Enforcement** → Rejects any commit or PR that violates traceability rules

## 🧪 CI Enforced Rules

- All requirements must be implemented and tested
- No implementation or test without a declared requirement
- Commit messages must reference at least one REQ-ID
- All functions and test cases must be annotated with REQ-ID
- Traceability matrix must be valid and complete

## 💻 Usage

```bash
pip install -r requirements.txt
pytest --cov=src
```
