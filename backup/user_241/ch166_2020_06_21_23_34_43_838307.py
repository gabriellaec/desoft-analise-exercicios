def total_do_semestre_por_bairro(dicionario):
    dicionario2 ={}
    x = dicionario.keys()
    for bairro in x:
        gasto = dicionario[bairro][6] + dicionario[bairro][7] + dicionario[bairro][8] + dicionario[bairro][9] + dicionario[bairro][10] + dicionario[bairro][11] 
        dicionario2[bairro] = gasto
    return dicionario2 