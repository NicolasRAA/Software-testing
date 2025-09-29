import pytest
from calc.operations import add

    # Arrange
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 0.5, 3.0),
    (-1.5, -2.5, -4.0),
])
def test_add_various(a, b, expected):
    # Act
    result = add(a, b)
    # Assert
    assert result == expected
