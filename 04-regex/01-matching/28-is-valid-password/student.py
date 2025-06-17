import re

def is_valid_password(string):
    pattern = (
        r'^(?=.*\d)'           # at least one digit
        r'(?=.*[a-z])'         # at least one lowercase
        r'(?=.*[A-Z])'         # at least one uppercase
        r'(?=.*[+\-*/.@])'     # at least one special character
        r'(?!.*(.)\1\1)'       # no three identical chars in a row
        r'(?!.*(.)\2\2\2)'     # no four identical chars anywhere
        r'.{12,}$'             # minimum length 12
    )
    return bool(re.fullmatch(pattern, string))
