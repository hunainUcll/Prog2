import pytest
from parentheses import matching_parentheses

# These should return True
@pytest.mark.parametrize('string', [
    "",         # empty string is valid
    "()",
    "(())",
    "(()())",
    "(((())))"
])
def test_matching_parentheses_valid(string):
    assert matching_parentheses(string), f"{string} contains equal number of closing and opening parenthesis"

# These should return False
@pytest.mark.parametrize('string', [
    "(",
    ")",
    "(()",
    "())",
    "())(()",
    "(()))("
])
def test_matching_parentheses_invalid(string):
    assert not matching_parentheses(string),f"{string} does not contains equal number of closing and opening parenthesis"
