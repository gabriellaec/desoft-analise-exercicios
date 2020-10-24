def calcula_media(dicionario):
    tudo = dicionario.items()
    notas = tudo.values()
    notas = sum(notas)
    media = notas/len(notas)
    return media