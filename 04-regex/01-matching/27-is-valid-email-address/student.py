# Write your code here
import re 

def is_valid_email_address(string):
    return re.fullmatch('.*@{1}(ucll.be|student.ucll.be)',string)