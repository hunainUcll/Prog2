import pytest
from mystatistics import average


@pytest.mark.parametrize("values, expected", [
    ([1, 1, 2], 1.3),
    ([2, 2, 2], 2),
    ([10, 10, 10], 10),
    ([0.1, 0.1, 0.1], 0.1),
])
def test_average_function(values, expected):
    assert average(values) == pytest.approx(expected,abs=0.1) 