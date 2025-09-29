import pytest
from calc.operations import pow_int

# Целочисленная степень: положительные и отрицательные показатели
    # Arrange
@pytest.mark.parametrize("base,exp,expected", [
    (2, 3, 8),
    (2, -1, 0.5),
    (-2, 3, -8),
    (-2, 2, 4),
])
def test_pow_int_various(base, exp, expected):
    # Act
    result = pow_int(base, exp)
    # Assert
    assert result == expected


# Ошибки в pow_int: 0 в отрицательной степени, и тип показателя
@pytest.mark.parametrize("base,exp,exc", [
    (0, -2, ZeroDivisionError),
    (2, 1.5, TypeError),
])
def test_pow_int_errors(base, exp, exc):
    # Arrange / Act / Assert
    with pytest.raises(exc):
        pow_int(base, exp)
