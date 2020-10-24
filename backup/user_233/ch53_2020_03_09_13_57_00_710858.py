def soma_impares(lista):
    
    soma = 0
    
    for i in lista:
        
        if i % 2 == 0: continue
        soma += i
   	
    return soma