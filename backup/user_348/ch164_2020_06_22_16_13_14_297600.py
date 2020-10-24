def traduz(palavras, tradução):
    lista_saida = []
    for i in palavras:
        if palavras[i] in tradução.keys():
            portugues = tradução[palavras[i]]
            lista_saida.append(portugues)
    return lista_saida
                