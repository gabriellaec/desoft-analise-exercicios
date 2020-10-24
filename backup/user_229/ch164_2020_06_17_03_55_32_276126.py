def traduz(palavras_ingles, ingles_portugues):
    tradução = []
    for palavra in palavras_ingles:
        if palavra in ingles_portugues:
            tradução.append(ingles_portugues[palavra])
    return tradução