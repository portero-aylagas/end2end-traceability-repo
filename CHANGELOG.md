# 📦 Changelog

## v1.0.0 — Initial Release

🔹 **Release Date:** 2025-05-13  
🔹 **Commit:** Initial full traceability commit (REQ-001 to REQ-005)

### ✨ Features

- ✅ Implemented calculator logic for:
  - REQ-001: Addition
  - REQ-002: Subtraction
  - REQ-003: Multiplication
  - REQ-004: Division
  - REQ-005: Input validation for numeric safety

- 🧪 Full unit test coverage (100%) across all REQs
- 📋 Traceability matrix auto-generation (`TRACEABILITY.md`)
- 📎 End-to-end REQ linking: `SPEC` → `REQ` → `Code` → `Test`
- 🔐 CI enforcement:
  - Commit message REQ tagging (`COMMIT_REQUIREMENT_ENFORCER.py`)
  - Code & test REQ matching
  - Function annotation validation
  - Test + implementation coverage checks
- 🧾 Summary reporting via GitHub Actions (`REQ_VALIDATION_REPORT.py`)

---

🔁 This version is CI-locked, fully auditable, and suitable for safety-critical traceability workflows.
