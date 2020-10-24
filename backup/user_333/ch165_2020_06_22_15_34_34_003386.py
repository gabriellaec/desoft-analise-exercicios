def mais_populoso(pais):
    mais_populoso = ''
    for estado in pais.keys():
        for cidade in pais[estado].keys():
            if mais_populoso!='' and pais[estado][cidade] > pais[estado][mais_populoso]:
                mais_populoso = cidade
            else:
                mais_populoso = cidade
                
    return mais_populoso
        