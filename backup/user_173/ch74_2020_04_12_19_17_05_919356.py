def conta_bigramas (s):
    lista = []
    dicionario = {}
    
    for i in range(len(s)):
        lista.append(s[i] + s[i+1])
                     
    for item in lista:
        dicionario[item] = lista.count(item)
        
    return dicionario