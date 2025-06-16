from itertools import permutations



def find_shortest_path(distance, city_count):
    cities = list(range(1,city_count))
    min_path = None
    min_total= float('inf')

    for perm in permutations(cities):
        path = [0]+list(perm)+[0]

        total = sum(distance(path[i],path[i+1])  for i in range(len(path)-1))

        if total < min_total:
            min_total = total
            min_path = path
    return min_path



