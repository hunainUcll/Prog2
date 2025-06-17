# Write your code here
import re

def ababa(string):
    return re.fullmatch('(.+)(.+)\\1\\2\\1',string)


"""Explanation:
(.+) → first group (A)

(.+) → second group (B)

\1 → repeats A

\2 → repeats B

\1 → repeats A again

^...$ → ensures the entire string matches ABABA"""