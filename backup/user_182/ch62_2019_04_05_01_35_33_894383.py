def filtra_positivos(x):
    lista=[]
    i=0
    
    while i<len(x):
        if x[i]>0:
            a=x[i]
            lista.append(a)
        i+=1
    return lista
y=[1,2,-1,-2]

print(filtra_positivos(y))

    