import pytest
from add import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 4, 7),
    (-2,2,0),

])
def test_add(a, b, expected):
    got = add(a, b)
    assert got == expected, f"Expected: {expected}, Got: {got}"
