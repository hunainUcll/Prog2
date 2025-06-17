
# Write your code here

import re 

def contains_three_digits(string):
    return re.fullmatch('.*\d.*\d.*\d',string)
