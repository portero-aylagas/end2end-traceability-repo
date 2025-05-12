# 📜 Process for End-to-End Traceability

1. Write high-level system specifications in `SPECIFICATION.md`.
2. Define atomic, testable requirements in `docs/requirements.md`.
3. Annotate each requirement with a unique `REQ-###` ID.
4. Implement logic in `src/` with REQ references in comments/docstrings.
5. Write tests in `tests/` that explicitly test those REQs.
6. Run the auto-generation script `GENERATE_TRACEABILITY_MATRIX.py`.
7. Submit a Git commit referencing REQ-ID(s).
8. CI will enforce all traceability rules before allowing a merge.
