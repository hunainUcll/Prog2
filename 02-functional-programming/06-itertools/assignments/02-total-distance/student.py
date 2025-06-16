from itertools import pairwise

def total_distance(path, distance):
    answer = 0 
    for a,b in pairwise(path):
        answer += distance(a,b)
    return answer