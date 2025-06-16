from itertools import groupby

def rle_encode(data):
    return ((char, sum(1 for _ in group)) for char, group in groupby(data))


def rle_decode(data):
    for char, count in data:
        for _ in range(count):
            yield char
