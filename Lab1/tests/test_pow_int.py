import pytest
from calc.operations import pow_int

# data driven Arrange
@pytest.mark.parametrize("base, exp, expected", [
    (2, 3, 8),
    (2, -1, 0.5),
    (-2, 3, -8),
    (-2, 2, 4),
])
def test_pow_int_various(base, exp, expected):
    # Act
    result = pow_int(base, exp)
    # Assert (AAA)
    assert result == expected


# границы 
    # Arrange vrode
@pytest.mark.parametrize("base, exp, exc", [
    (0, -2, ZeroDivisionError),  # 0 в отрицательной степени
    (2, 1.5, TypeError),         # показатель должен быть int
])
def test_pow_int_errors(base, exp, exc):
    # Act + Assert
    with pytest.raises(exc):
        pow_int(base, exp)


def test_pow_int_zero_base_zero_exp():
    # Arrange
    base, exp = 0, 0
    # Act + Assert
    assert pow_int(base, exp) == 1  # в Python 0**0 == 1

def test_pow_int_zero_base_positive_exp():
    # Arrange
    base, exp = 0, 5
    # Act + Assert
    assert pow_int(base, exp) == 0

def test_pow_int_zero_base_negative_exp_raises():
    # Arrange / Act + Assert
    with pytest.raises(ZeroDivisionError):
        pow_int(0, -1)
