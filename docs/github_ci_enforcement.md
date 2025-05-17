# 🔐 GitHub CI Enforcement Configuration

To fully enforce the CI-based traceability system, configure your GitHub repository with the following settings:

## 🛡️ Branch Protection Rules

- **Protect `main` branch**  
- Enable: ✅ Require pull request before merging  
- Enable: ✅ Require status checks to pass before merging  
  - Required check: `verify` (from CI)  
- Enable: ✅ Require branches to be up to date before merging  
- Enable: ✅ Require linear history  
- Enable: ✅ Require signed commits (optional but recommended)  
- Enable: ✅ Lock branch (read-only, force PRs only)

## ✅ Required GitHub Actions Jobs

- Name: `verify`
- Enforces:
  - Commit REQ-ID validation
  - Code/test REQ coverage
  - Traceability matrix validity
  - 100% test coverage
  - Logging and artifact generation

## 🗂️ Summary Output

- Coverage and REQ matrix summary appears in PR UI via `REQ_VALIDATION_REPORT.py`.
- CI must export artifacts: coverage reports, traceability matrix, and enforcement logs.
