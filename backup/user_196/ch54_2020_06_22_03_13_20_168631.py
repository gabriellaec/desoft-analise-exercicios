def calcula_fibonacci(n):
    listafinal = []
    f1 = 1 
    f2 = 1
    if (n < 1): 
        return 
    for i in range (n+1):
        f1 = f2
        soma = f1+f2
        f2 = soma
        listafinal.append(soma)        
    return listafinal
 