def monta_dicionario(lista1, lista2):
    
    dicionario = {}
    
    i = 0
    
    for e in lista1:
        
        dicionario[e] = lista2[i]
        
        i += 1
        
    return dicionario
        