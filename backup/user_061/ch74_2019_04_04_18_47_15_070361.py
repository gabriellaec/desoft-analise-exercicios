def acha_bigramas(string):
    lista = []
    i = 0
    while i < len(string)-1:
        bigrama = string[i]+string[i+1]
        lista.append(bigrama)
        i+=1
    return lista

def conta_bigramas(frase):
    lista = acha_bigramas(frase)
    dicionario = {}
    i = 0
    while i<len(lista):
        bigrama = lista[i]
        if bigrama not in dicionario:
            dicionario[bigrama] = 1
        elif bigrama in dicionario:
            dicionario[bigrama] += 1
        i+=1
    return dicionario