def total_do_semestre_por_bairro(dicionario):
    dicionario2 = {}
    for k in dicionario:
        for v in range(6, 12):
            dicionario2[k] = dicionario[k][v]
            dicionario2[k] += dicionario[k][v]
                
    return dicionario2
