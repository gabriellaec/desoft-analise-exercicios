def acha_bigramas(x):
    i = 0
    lis = []
    while i < len(x)-1:
        y = (x[i] + x[i+1])
        if y not in lis:
        	lis.append(y)
        i +=1
    return lis
