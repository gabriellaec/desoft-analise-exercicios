def calcula_media(dicionario):
    notas = dicionario.values()
    notas = sum(notas)
    media = notas/len(notas)
    return media