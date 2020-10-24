def interseccao_valores(dicio1, dicio2):
    valores_comum = []
    for v1 in dicio1.values():
        if v1 in dicio2.values():
            valores_comum.append(v1)
    return valores_comum