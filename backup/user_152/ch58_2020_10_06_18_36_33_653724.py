def conta_a(palavra):
    n = 0
    i = 0
    while i <len(palavra):
        if palavra[i] == "a":
            n += 1
        i += 1
    return n