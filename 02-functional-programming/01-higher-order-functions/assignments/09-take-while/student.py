def take_while(xs, condition):
    A = list()
    for i,element in enumerate(xs):
        if condition(element):
           A.append(element)
        else:
            return (A,xs[i:])
    return (A,[])
