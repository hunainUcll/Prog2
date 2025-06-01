def find(collection,function):
    for element in collection:
        if function(element):
            return element
    return None

