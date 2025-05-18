# ✅ Requirements — Functional + Infrastructure

## Functional Requirements

| ID        | Description                                      | Related Spec ID |
|-----------|--------------------------------------------------|-----------------|
| REQ-001   | The system shall add two numbers.                | SPEC-001        |
| REQ-002   | The system shall subtract two numbers.           | SPEC-001        |
| REQ-003   | The system shall multiply two numbers.           | SPEC-001        |
| REQ-004   | The system shall divide two numbers.             | SPEC-001        |
| REQ-005   | The system shall reject non-numeric inputs.      | SPEC-002        |

## Infrastructure Requirements

| ID           | Description                                                                 | Related Spec ID  |
|--------------|-----------------------------------------------------------------------------|------------------|
| REQ-INF-001  | CI must run on `push` and `pull_request` events targeting `main`.           | SPEC-INF-001     |
| REQ-INF-002  | CI must reject commits without a REQ-ID reference.                          | SPEC-INF-004     |
| REQ-INF-003  | CI must verify REQ-IDs exist in `requirements.md`.                          | SPEC-INF-002     |
| REQ-INF-004  | CI must enforce that REQ-IDs are covered in both code and tests.            | SPEC-INF-003     |
| REQ-INF-005  | GitHub must enforce PR + CI pass before merge to `main`.                    | SPEC-INF-005     |
| REQ-INF-006  | GitHub must lock `main` and reject direct pushes.                           | SPEC-INF-006     |
| REQ-INF-007  | CI must post a coverage + REQ table to GitHub PR view.                      | SPEC-INF-007     |
| REQ-INF-008  | CI must export traceability and test artifacts.                             | SPEC-INF-008     |
| REQ-INF-009  | CI must validate commit messages and PR titles contain valid REQ-IDs.       | SPEC-INF-009     |                     
| REQ-INF-010  | All enforcement scripts must include logging for auditability.                                        | SPEC-INF-010 |
| REQ-INF-011  | The system shall allow REQs to be declared before implementation, but block untested implementations. | SPEC-INF-011 |
| REQ-INF-012  | CI must dynamically generate the traceability matrix at runtime only.                                 | SPEC-INF-012 |
| REQ-INF-013  | Traceability matrix files must be excluded from version control (e.g., `.gitignore`).                 | SPEC-INF-013 |

