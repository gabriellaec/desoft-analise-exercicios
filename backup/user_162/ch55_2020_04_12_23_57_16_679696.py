def encontra_maximo(m): 
    max_por_linha = []
    for i in m:
        for j in i:
            max_por_linha.append(j**2)
    return int(max(max_por_linha)**0.5)