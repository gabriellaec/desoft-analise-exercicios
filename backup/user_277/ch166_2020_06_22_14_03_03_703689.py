def total_do_semestre_por_bairro(dicionario):
    dicionario2 = {}
    
    for bairro in dicionario:
        soma = 0
        gasto_anual = dicionario[bairro]
        gasto_semestral = gasto_anual[6:]
        for i in range(len(gasto_semestral)):
            soma = soma + gasto_semestral[i]
        dicionario2[bairro] = soma
        print(dicionario2)
    return dicionario2

