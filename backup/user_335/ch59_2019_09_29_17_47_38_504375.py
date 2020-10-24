def conta_a (string):
    a = 0
    i = 0
    while i < len(string):
        if string[i] == "a":
            a += 1
            i += 1
        else:
            i += 1
    return a