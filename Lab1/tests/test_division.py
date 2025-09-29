import pytest
from calc.operations import div

# Базовые случаи деления + десятичные
    # Arrange
@pytest.mark.parametrize("a,b,expected", [
    (9, 4, 2.25),
    (-8, 2, -4),
    (7.5, 2.5, 3.0),
])
def test_div_various(a, b, expected):
    # Act
    result = div(a, b)
    # Assert
    assert result == expected


# Деление на ноль — граничный случай с исключением
@pytest.mark.parametrize("a", [0, 1, -5, 3.14])
def test_div_by_zero_raises(a):
    # Arrange / Act / Assert
    with pytest.raises(ZeroDivisionError):
        div(a, 0)
