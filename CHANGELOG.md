# 📦 Changelog

## v1.0.1 — GitHub Protections & Infrastructure Traceability

🔹 **Release Date:** 2025-05-16  
🔹 **Commit:** `0666a01`  
🔹 **Summary:** Hardened the repository with GitHub branch protections and made infrastructure requirements fully traceable.

### 🔧 Improvements

- ✅ Enforced **GitHub-side protections**:
  - Locked `main` branch (no direct pushes)
  - Required pull requests for all merges
  - Required status check: `CI / verify`

- ✅ CI validation fixes:
  - Commit message validation improved for pull requests
  - Resolved commit message parsing via `GITHUB_ENV`
  - Added test triggers to register GitHub status check `verify`

- ✅ New infrastructure REQs:
  - `REQ-INF-001`: CI runs on pull_request targeting main
  - `REQ-INF-002`: Commit messages must reference a valid REQ
  - `REQ-INF-003`: All CI steps must validate traceability

- 📋 Updated:
  - `requirements.md` with `REQ-INF-XXX` entries
  - `TRACEABILITY.md` to include CI/tooling REQs
  - `README.md` to reflect enforcement guarantees

---

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

🔁 All releases are CI-locked, traceable, and auditable for safety-critical development.
