def calcula_media(dicionario):
    tudo = dicionario.itens()
    notas = tudo.values()
    notas = sum(notas)
    media = notas/len(notas)
    return media