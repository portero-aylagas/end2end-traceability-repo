# 📋 Traceability Matrix

| Spec ID       | Req ID        | Code Module                     | Test Case                           |
|---------------|---------------|----------------------------------|-------------------------------------|
| SPEC-001      | REQ-001       | src/calculator.py::REQ-001       | tests/test_calculator.py::REQ-001  |
| SPEC-001      | REQ-002       | src/calculator.py::REQ-002       | tests/test_calculator.py::REQ-002  |
| SPEC-001      | REQ-003       | src/calculator.py::REQ-003       | tests/test_calculator.py::REQ-003  |
| SPEC-001      | REQ-004       | src/calculator.py::REQ-004       | tests/test_calculator.py::REQ-004  |
| SPEC-002      | REQ-005       | src/calculator.py::REQ-005       | tests/test_calculator.py::REQ-005  |
| SPEC-INF-001  | REQ-INF-001   | .github/workflows/ci.yml         | ✅ (CI Workflow trigger logic)     |
| SPEC-INF-004  | REQ-INF-002   | COMMIT_REQUIREMENT_ENFORCER.py   | ✅ Regex enforcement logic         |
| SPEC-INF-002  | REQ-INF-003   | REQUIREMENT_COVERAGE_CHECK.py    | ✅ requirements cross-check       |
| SPEC-INF-003  | REQ-INF-004   | REQUIREMENT_COVERAGE_CHECK.py    | ✅ coverage scan                  |
| SPEC-INF-005  | REQ-INF-005   | 📘 GitHub UI setting             | N/A                                 |
| SPEC-INF-006  | REQ-INF-006   | 📘 GitHub branch lock            | N/A                                 |
| SPEC-INF-007  | REQ-INF-007   | REQ_VALIDATION_REPORT.py         | ✅ step summary table             |
| SPEC-INF-008  | REQ-INF-008   | coverage.xml, htmlcov/           | ✅ artifacts in CI                 |
| SPEC-INF-009  | REQ-INF-009   | COMMIT_REQUIREMENT_ENFORCER.py   | ✅ REQ-ID validation              |
| SPEC-INF-010  | REQ-INF-010   | *_CHECK.py, *_SCAN.py            | ✅ logging verified                |
