def calcula_total_da_nota (lista1, lista2):
    soma= 0 
    lista_total= []
    
    i= 0 
    while i < len(lista1):
        i = lista[i]*lista2[i]
        lista_total.append(i)
        i= i + 1 
    
    for valores in lista_total:
        soma= soma + valores
        return soma
    