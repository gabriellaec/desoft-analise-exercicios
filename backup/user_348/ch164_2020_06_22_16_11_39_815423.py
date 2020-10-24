def traduz(palavras, tradução):
    lista_saida = []
    for i in palavras:
        for ingles, portugues in tradução.items():
            if palavras[i] in tradução.keys():
                lista_saida.append(portugues)
    return lista_saida
                