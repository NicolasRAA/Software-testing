from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    return a + b

def sub(a: Number, b: Number) -> Number:
    return a - b

def mul(a: Number, b: Number) -> Number:
    return a * b

def div(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def pow_int(base: Number, exp: int) -> Number:
    if not isinstance(exp, int):
        raise TypeError("exp must be int")
    if base == 0 and exp < 0:
        raise ZeroDivisionError("0 cannot be raised to a negative power")
    return base ** exp

def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be >= 0")
    res = 1
    for k in range(2, n + 1):
        res *= k
    return res
