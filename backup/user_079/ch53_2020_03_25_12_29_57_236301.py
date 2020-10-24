def soma impares(x):
    i=0
    y=[]
    while i<len(x):
        if x[i]%2 != 0:
            y.append(x[i])
        i+=1
    print(sum(y))
            