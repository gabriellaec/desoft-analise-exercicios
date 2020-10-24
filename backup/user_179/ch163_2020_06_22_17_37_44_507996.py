def calcula_media(lista):
    notas = []
    for i in range(len(lista)):
        dicionario = lista[i]
        notas.append(dicionario.values())
    notas = sum(notas)
    media = notas/len(notas)
    return media