def rle_encode(data):
    iterator = iter(data)
    try:
        current = next(iterator)
    except StopIteration:
        return  # gracefully exit the generator
    
    count = 1
    for char in iterator:
        if char == current:
            count += 1
        else:
            yield (current, count)
            current = char
            count = 1
    yield (current, count)

def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char
