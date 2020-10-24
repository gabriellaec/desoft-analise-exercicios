def calcula_fibonacci(n):
    listafinal = []
    f1 = 1 
    f2 = 1
    if (n == 1): 
        listafinal.append(1)
    for i in range (2, n+1):
        f1 = f2
        soma = f1+f2
        f2 = soma
        listafinal.append(soma)        
    return listafinal
 