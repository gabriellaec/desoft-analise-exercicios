def traduz(lista_palavras_em_ingles, dicio_kingles_vtradu):
    minha_lista = []
    c = 0
    while c < len(lista_palavras_em_ingles):
        for word,tradu in dicio_kingles_vtradu.items():
            if lista_palavras_em_ingles[c] == word:
                minha_lista.append(tradu)
    return minha_lista          
    