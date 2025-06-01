def partition(collection,function):
    A = []
    B = []
    for element in collection:
        if function(element):
            A.append(element)
        else:
            B.append(element)

    return (A, B)