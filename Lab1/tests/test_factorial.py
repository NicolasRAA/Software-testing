import pytest
from calc.operations import factorial

# Факториал: базовые и малые значения
    # Arrange
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
])
def test_factorial_small(n, expected):
    # Act
    result = factorial(n)
    # Assert
    assert result == expected
    

# Ошибки factorial: отрицательные и неверный тип
    # Arrange
@pytest.mark.parametrize("n,exc", [
    (-1, ValueError),
    (2.5, TypeError),
])
def test_factorial_errors(n, exc):
    # Act / Assert
    with pytest.raises(exc):
        factorial(n)
