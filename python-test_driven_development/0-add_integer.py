#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the integer addition of a and b
    Raises:
    TypeError: If a or b is not integer or not float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (a + b)
