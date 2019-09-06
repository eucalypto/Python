def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """

    :rtype: object
    """
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
