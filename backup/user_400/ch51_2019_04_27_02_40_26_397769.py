def estritamente_crescente(x):
    i = 1
    while i < len(x):
        if x[i] <= x[i-1]:
            del x[i]
        else:
            i += 1
    return x
