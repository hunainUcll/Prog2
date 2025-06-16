def countX(text):
    count = 0
    if text == "":
        return 0
    else:
        if text[0] == "x":
            count = 1
        return count + countX(text[1:])
    
        