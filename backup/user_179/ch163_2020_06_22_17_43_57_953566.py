def calcula_media(lista):
    notas = []
    for i in range(len(lista)):
        dicionario = lista[i]
        valores = dicionario.values()
        notas.append(valores)
    notas_total = sum(notas)
    print(notas)
    media = notas_total/len(notas)
    return media