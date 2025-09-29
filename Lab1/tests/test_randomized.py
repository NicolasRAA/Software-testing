import math
import random
from calc.operations import add, mul

def test_add_mul_randomized_isclose():
    # Arrange
    rng = random.Random(42)  # seed

    for _ in range(100):
        a = rng.uniform(-1e3, 1e3)
        b = rng.uniform(-1e3, 1e3)

        # Act
        s = add(a, b)
        p1 = mul(a, 1.0)
        p0 = mul(a, 0.0)

        # Assert
        # (a + b) - a == b с допуском
        assert math.isclose(s - a, b, rel_tol=1e-12, abs_tol=1e-12)
        # a * 1 == a
        assert math.isclose(p1, a, rel_tol=1e-12, abs_tol=1e-12)
        # a * 0 == 0
        assert math.isclose(p0, 0.0, rel_tol=1e-12, abs_tol=1e-12)
