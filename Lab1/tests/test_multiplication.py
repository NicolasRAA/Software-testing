import pytest
from calc.operations import mul

@pytest.mark.parametrize("a,b,expected", [
    (123, 0, 0),
    (0, 999, 0),
    (-4, 2.5, -10.0),
    (-3, -2, 6),
    (1.2, 3, 3.6),
])
def test_mul_various(a, b, expected):
    # Arrange

    # Act
    result = mul(a, b)

    # Assert
    # сравнение с допуском для порхождения упавшего теста
    assert result == pytest.approx(expected, rel=1e-12, abs=1e-12)
