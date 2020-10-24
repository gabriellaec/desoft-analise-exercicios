def calcula_fibonacci(F):
    F1=1
    F2=1
    lista=[]
    i=0
    while i<len(lista):
        F[i]=F[i-1]+F[i-2]
        lista.append(F[i])
        i=i+1
    return(lista)
        
        