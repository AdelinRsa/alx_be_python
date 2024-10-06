# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform arithmetic operation based on the given parameters.
    
    Args:
    num1 (float): The first number
    num2 (float): The second number
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float: The result of the operation, or a string in case of an error
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
