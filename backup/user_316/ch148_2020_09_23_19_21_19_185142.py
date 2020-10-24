def popular_lista(palavra):
    lista = []
    for c in palavra:
        lista.append(c)
    return lista

def conta_letras(palavra):
    lista = popular_lista(palavra)
    dicionario = {}
    for i in range(len(lista)):
        if lista[i] not in dicionario:
            dicionario[lista[i]] = lista.count(lista[i])
            
    return dicionario