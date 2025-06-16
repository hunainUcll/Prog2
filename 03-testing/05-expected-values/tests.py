# tests.py

import pytest
from mergesort import split_in_two
from mergesort import merge_sorted
from itertools import permutations
from mergesort import merge_sort

@pytest.mark.parametrize("ns", [list(range(n)) for n in range(101)])  # Lists of length 0 to 100
def test_split_in_two(ns):
    left, right = split_in_two(ns)

    # Test 1: Combined result must equal the original list
    assert left + right == ns

    # Test 2: Lengths must differ by at most one
    assert abs(len(left) - len(right)) <= 1


import pytest
from mergesort import merge_sorted

@pytest.mark.parametrize("left", [
    [], [1], [2, 5], [4, 10, 15], [2, 5, 5, 9], [0, 1, 3]
])
@pytest.mark.parametrize("right", [
    [], [1], [3, 6], [4, 10, 15], [2, 5, 5, 9], [2, 3, 4]
])
def test_merge_sorted(left, right):
    result = merge_sorted(left, right)
    assert result == sorted(left + right)



@pytest.mark.parametrize("expected", [
    [],
    [1],
    [1, 1],
    [1, 2],
    [1, 2, 3],
    [4, 4, 4],
    [0, 2, 4]
])
def test_merge_sort(expected):
    for ns in permutations(expected):
        assert merge_sort(list(ns)) == expected
