def is_palindrom(string):
    return string == string[::-1]

def indices_of(xs, condition):
    indices = []
    for index, string in enumerate(xs):
        if condition(string):
            indices.append(index)
    return indices