def soma_valores(lista):
    
    num_lista = len(lista)
    soma = 0
    i=0
    
    while i < num_lista:
        soma += lista[i]
        i+=1
    return soma