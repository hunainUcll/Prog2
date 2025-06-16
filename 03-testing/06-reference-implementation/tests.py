import pytest
from search import linear_search, binary_search, Student

@pytest.mark.parametrize('students,target_id', [
    ([Student(1)], 1),                      # single match
    ([Student(1)], 2),                      # single no match
    ([Student(1), Student(3), Student(5)], 3),  # middle match
    ([Student(1), Student(3), Student(5)], 4),  # no match
    ([Student(i) for i in range(10)], 0),   # first element
    ([Student(i) for i in range(10)], 9),   # last element
    ([Student(i) for i in range(10)], 5),   # middle element
    ([Student(i) for i in range(10)], 11),  # out of range
    ([], 1),                                 # empty list
])
def test_search(students, target_id):
    assert linear_search(students, target_id) == binary_search(students, target_id)
