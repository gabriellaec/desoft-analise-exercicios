def traduz(palavras, tradução):
    lista_saida = []
    for i in palavras:
        for ingles in tradução.keys():
            if ingles == palavras[i]:
                portugues = tradução[ingles]
                lista_saida.append(portugues)
    return lista_saida

def traduz (lista, dicionario):
    lista_saida = []
    i = 0
    while i < len(lista):
        for ingles in dicionario.keys():
            if ingles == lista[i]:
                lista_saida.append(dicionario[ingles])
        i = i + 1
    return lista_saida