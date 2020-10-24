def encontra_maximo(m): 
    max_por_linha = []
    for i in m:
        max_por_linha.append(max(i))
    return max(max_por_linha )