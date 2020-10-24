def estritamente_crescente(x):
    a = []
    i=0
    while i<len(x):
        if x[i] == x[i-1] == x[i+1] or x[i] < x[i+1]:
            a.append(x[i])
        i+=1
    return a