"""
Fault-tolerant calculator with input validation and logging.
"""

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# REQ-001
def add(a, b):
    validate_inputs(a, b, "add")
    result = a + b
    logging.info(f"Add: {a} + {b} = {result}")
    return result

# REQ-002
def subtract(a, b):
    validate_inputs(a, b, "subtract")
    result = a - b
    logging.info(f"Subtract: {a} - {b} = {result}")
    return result

# REQ-003
def multiply(a, b):
    validate_inputs(a, b, "multiply")
    result = a * b
    logging.info(f"Multiply: {a} * {b} = {result}")
    return result

# REQ-004
def divide(a, b):
    validate_inputs(a, b, "divide")
    if b == 0:
        logging.error("Divide: Attempt to divide by zero.")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"Divide: {a} / {b} = {result}")
    return result

# REQ-005
def validate_inputs(a, b, operation):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        logging.error(f"{operation}: Invalid input types: {a} ({type(a)}), {b} ({type(b)})")
        raise TypeError("Inputs must be numeric")