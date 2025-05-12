# 🧱 Architecture

All functionality is encapsulated in a single module: `src/calculator.py`.

- `add(a, b)` → REQ-001
- `subtract(a, b)` → REQ-002
- `multiply(a, b)` → REQ-003
- `divide(a, b)` → REQ-004 (with error handling)

Tests live in `tests/test_calculator.py` and follow one-to-one mapping with REQs.
