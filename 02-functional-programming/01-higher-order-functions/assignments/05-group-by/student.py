def group_by(xs, key_function):
    result = {}
    for element in xs:
        key = key_function(element)
        if key not in result:
            result[key] = []
        result[key].append(element)
    return result
            
