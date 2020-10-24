def traduz(palavras, tradução):
    lista_saida = []
    for i in palavras:
        for ingles in tradução.keys():
            if ingles == palavras[i]:
                lista_saida.append(tradução[ingles])
    return lista_saida

