def total_do_semestre_por_bairro(dic_bairros):
    valor_gasto_semestre = {}
    for bairro, valores in dic_bairros.items():
        total_gasto = 0
        valores = valores[::-1]
        for i in range(6):
            total_gasto += valores[i]
        valor_gasto_semestre[bairro] = total_gasto
    return valor_gasto_semestre