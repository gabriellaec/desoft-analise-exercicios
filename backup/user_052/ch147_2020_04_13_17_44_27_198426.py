def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    a = dicionario.values()
    lista2 = []
    for x in a:
        b = max(x)
        lista2[i] = b
        return lista2[i]
    
        
        