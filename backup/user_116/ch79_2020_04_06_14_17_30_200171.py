
def monta_dicionario(lista1,lista2):
    dicionario={}
    
    for e , n in zip(lista1,lista2):    
        dicionario[e]=n
    return dicionario 
