def calcula_fibonacci(n):
    listafinal = []
    f1 = 1 
    f2 = 1
    if (n < 1): 
        return False 
    for i in range (0, n+1):
        f1 = f2
        soma = f1+f2
        f2 = soma
        listafinal.append(soma)        
    return listafinal
 