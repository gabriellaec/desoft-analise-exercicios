def calcula_Fibonacci(n):
    F1=1
    F2=1
    lista=[]
    i=0
    while i<int(n):
        F[i]=F[i-1]+F[i-2]
        lista.append(F[i])
        i=i+1
    return(lista)
        
        