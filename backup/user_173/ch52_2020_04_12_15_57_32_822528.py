def calcula_total_da_nota (lista1,lista2):
    preco_final = 0
    i = 0
    while i < len(lista1):
        preco_final += lista1[i]*lista2[i]        
        i += 1            
    
    return preco_final
            
           