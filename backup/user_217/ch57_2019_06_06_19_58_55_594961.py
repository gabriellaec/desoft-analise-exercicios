def soma_impares(lista):
    
    lista_impar = []
    i = 0
    
    while i < len(lista):
       if lista[i] % 2 != 0:           
           lista_impar.append(lista[i])
       i = i + 1 
     
    return sum(lista_impar)
       