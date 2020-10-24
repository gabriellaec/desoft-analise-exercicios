def estritamente_crescente(x):
    for i in range(1, len(x)):
        if x[i]<x[i-1]:
            del x[i]
    return x