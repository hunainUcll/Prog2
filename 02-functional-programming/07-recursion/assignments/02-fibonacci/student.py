def fibonacci(number):
    ## first base case 
    if number < 0:
        return 0
    if number == 0:
        return 0
    if number ==1:
        return 1
    else: 
        return fibonacci(number - 1) + fibonacci(number - 2)