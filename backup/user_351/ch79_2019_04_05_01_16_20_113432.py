def monta_dicionario(lista_chaves,lista_valores):
    dicionario={}
    for e in lista_chaves:
        dicionario[lista_chaves[e]]=[lista_valores[e]]
    return dicionario
        
        
        