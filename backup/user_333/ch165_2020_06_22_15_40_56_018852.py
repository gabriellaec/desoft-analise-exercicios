def mais_populoso(pais):
    lista_estados=pais.keys()
    lista_populacao=[]
    for estado in pais.keys():
        populacao_total = 0
        for populacao in pais[estado].values():
            populacao_total+=populacao
        lista_populacao.append(populacao_total)
    
    mais_populoso = lista_estados(lista_populacao.index(max(lista_populacao)))
    
    return mais_populoso
        