def traduz(lista_ingles, dicionario_pt):
    lista_traducao = []
    for p in lista_ingles:
        if p in dicionario_pt:
            lista_traducao.append(dicionario_pt[p])
    
    return lista_traducao