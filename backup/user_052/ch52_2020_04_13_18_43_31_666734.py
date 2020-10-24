def calcula_total_da_nota (lista1,lista2):
    #lista1 preço produto
    #lista2 quantidade
    i = 0
    preço = 0
    while i < len(lista1):
        preço = lista1[i] *lista2[i]
        i =+ 1
    return preço
        
    