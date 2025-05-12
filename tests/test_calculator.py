import pytest
from src import calculator

# REQ-001
def test_add():
    assert calculator.add(2, 3) == 5

# REQ-002
def test_subtract():
    assert calculator.subtract(5, 3) == 2

# REQ-003
def test_multiply():
    assert calculator.multiply(4, 2) == 8

# REQ-004
def test_divide():
    assert calculator.divide(10, 2) == 5

# REQ-004
def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

# REQ-005
def test_validate_inputs_invalid_type():
    from src.calculator import validate_inputs
    import pytest
    with pytest.raises(TypeError):
        validate_inputs("x", 10, "add")        
