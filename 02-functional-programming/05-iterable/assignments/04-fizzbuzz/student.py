def fizzbuzz():
    count = 1
    while True:
        if count % 3 == 0 and count % 5 == 0:
            yield "fizzbuzz"
        elif count % 3 == 0:
            yield "fizz"
        elif count % 5 == 0:
            yield "buzz"
        else:
            yield str(count)
        count += 1
