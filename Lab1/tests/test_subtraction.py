import pytest
from calc.operations import sub

    # Arrange
@pytest.mark.parametrize("a,b,expected", [
    (10, 7, 3),
    (3, 8, -5),
    (-2, -5, 3),
    (2.5, 0.5, 2.0),
])
def test_sub_various(a, b, expected):
    # Act
    result = sub(a, b)
    # Assert
    assert result == expected
