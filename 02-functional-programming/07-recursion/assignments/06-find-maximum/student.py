def findMaximum(lst):
    if len(lst) == 0:
        raise IndexError("Cannot find maximum of an empty list")

    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = findMaximum(lst[1:])
        print(max_of_rest)
        if lst[0] > max_of_rest:
            return lst[0]
        else:
            return max_of_rest
        


print(findMaximum([10,9,8,7]))