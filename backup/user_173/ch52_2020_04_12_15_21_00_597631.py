def calcula_total_da_nota (lista1,lista2):
    preço = 0
    preco_final = 0
    i = 0
    while i < len(lista1):
        preco = lista1[i]
        i += 1
        ii = 0
        while i < len(lista2):
            preco_final = (lista1[i])*(lista2[ii])
            ii += 1
    
    return preco_final
            
           