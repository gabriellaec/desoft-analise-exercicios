def calcula_euler(x, n):
    lista=[0]*n
    i = 0
    contador = 0
    soma = 0
    while i < n:  
        lista[i] = (x**contador)/math.factorial(contador)
        soma += lista[i]
        i += 1
        contador += 1
    
    return soma
    
    
    
    
    
    
    
    
    
print (calcula_euler(5,4)
    