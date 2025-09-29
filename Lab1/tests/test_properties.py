import pytest
from calc.operations import add, mul

# Коммутативность сложения
@pytest.mark.parametrize("a,b", [(0,0),(1,2),(-3,4),(2.5,-0.5)])
def test_add_commutative(a, b):
    # Arrange / Act
    r1 = add(a, b)
    r2 = add(b, a)
    # Assert
    assert r1 == r2

# Коммутативность умножения
@pytest.mark.parametrize("a,b", [(0,0),(1,2),(-3,4),(2.5,-0.5)])
def test_mul_commutative(a, b):
    # Arrange / Act
    r1 = mul(a, b)
    r2 = mul(b, a)
    # Assert
    assert r1 == r2

# Дистрибутивность a*(b+c) == a*b + a*c
@pytest.mark.parametrize("a,b,c", [(1,2,3),(2,-1,5),(0,4,-2),(-2,3,1.5)])
def test_distributive(a, b, c):
    # Arrange / Act
    left = mul(a, add(b, c))
    right = add(mul(a, b), mul(a, c))
    # Assert
    assert left == right
