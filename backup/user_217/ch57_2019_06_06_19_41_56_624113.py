def soma_impares(lista):
    
    lista_impar = []
    i = 0
    
    while i < len(lista):
       lista_impar.append(lista[i])
       i = i + 2
       
    return sum(lista_impar)