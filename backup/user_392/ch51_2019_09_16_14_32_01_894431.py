def estritamente_crescente(x):
    lis = []
    i = 0
    while i < len(x):
        if x[i] > x[i+1]:
            lis.append(x[i])
        elif x[i+1] > x[i]:
            lis.append(x[i+1])
        else:
            lis.append(x[i])
        i+=1
    return lis   
