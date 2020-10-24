def pos_arroba (x):
    i = 0
    pos = -1
    n = len(x)
    while i < n:
        if x[i] == "@":
            pos = i
        i+=1
    return pos
