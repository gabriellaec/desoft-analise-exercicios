def simplifica_dict(dicio):
    lista_chaves = []
    lista_valores = []
    lista_total = []
    lista_limpinha = []
    
    for chaves in dicio.keys():
        lista_chaves.append(chaves)
        lista_total.append(chaves)
    
    for valores in dicio.values():
        lista_valores.append(valores)
        lista_total.append(valores)
        
    setado = set(lista_total)
    lista_limpinha = list(setado)
    
    #return lista_chaves, lista_valores, lista_total
    return lista_limpinha