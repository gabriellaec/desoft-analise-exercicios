def estritamente_crescente(x):
    i=0
    while i<len(x):
        if x[i]<x[i+1]:
            x.remove(x[i])
        i+=1
    return x