def total_do_semestre_por_bairro(dicionario):
    dicionario2 = {}
    soma = 0
    for bairro in dicionario:
        gasto_anual = dicionario[bairro]
        gasto_semestral = gasto_anual[:6]
        for i in range(0,6):
            soma = soma + gasto_semestral[i]
        dicionario2[bairro] = soma
    return dicionario2