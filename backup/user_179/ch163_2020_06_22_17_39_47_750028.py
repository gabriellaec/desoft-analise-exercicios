def calcula_media(lista):
    notas = []
    for i in range(len(lista)):
        dicionario = lista[i]
        notas.append(dicionario.values())
    notas_total = sum(notas)
    media = notas/len(notas)
    return media