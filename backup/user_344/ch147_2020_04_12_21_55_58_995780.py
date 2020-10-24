def mais_frequente(lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] +=1
            
    lista = list(dicionario.keys())
    lista2 = list(dicionario.values())
    
    return lista[lista2.index(max(lista2))]
    