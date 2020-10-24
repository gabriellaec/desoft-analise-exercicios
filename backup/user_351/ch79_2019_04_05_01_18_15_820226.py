def monta_dicionario(lista_chaves,lista_valores):
    dicionario={}
    i=0
    while i<len(lista_chaves):
        dicionario[lista_chaves[i]]=[lista_valores[i]]
        i+=1
    return dicionario
        
        
        