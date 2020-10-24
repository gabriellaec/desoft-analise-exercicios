def total_do_semestre_por_bairro(dicio):
    dicionario = {}
    for k in dicio:
        for i in range(6,12):
            if not k in dicionario:
                dicionario[k] = dicionario[k][i]
            else:
                dicionario[k] = += dicionario[k][i]
    return dicionario