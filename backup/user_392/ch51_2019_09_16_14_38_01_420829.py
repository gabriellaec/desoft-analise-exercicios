def estritamente_crescente(x):
    lis = []
    i = 0
    lis.append(x[0])
    while i < len(x)-2:
        if x[i+1] > x[i]:
            lis.append(x[i+1])
        i+=1
    return lis   
