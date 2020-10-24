def soma_impares(a):
    b=[]
    for i in range(len(a)):
        if a[i]%2!=0:
            b.append(a[i])
    return b