def traduz(palavras, tradução):
    lista_saida = []
    for i in palavras:
        for ingles in tradução.keys():
            if ingles == palavras[i]:
                portugues = tradução[ingles]
                lista_saida.append(portugues)
    return lista_saida