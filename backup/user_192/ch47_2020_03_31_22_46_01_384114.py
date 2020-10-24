def estritamente_crescente(x):
    a = []
    i=0
    while i<len(x):
        if x[i-1] < x[i] and x[i-1] == x[i]:
            a.append(x[i])
        i+=1
    return a