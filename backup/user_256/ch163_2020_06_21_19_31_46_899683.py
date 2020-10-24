def calcula_media(lista):
    notas = []
    for dicionarios in lista:
        for valores in dicionarios.values():
            notas.append(valores)
    media = sum(notas)/len(notas)
    return media
            