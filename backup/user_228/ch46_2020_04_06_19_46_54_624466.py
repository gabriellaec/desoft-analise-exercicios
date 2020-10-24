def numero_no_indice(a):
    b=[]
    for i in range(len(a)):
        if i==a[i]:
            b.append(a[i])
            
    return b