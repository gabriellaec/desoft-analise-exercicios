def total_do_semestre_por_bairro(infra):
    total = {}
    for bairro, gastos in infra.items():
        soma = 0
        for i in range(5,12):
            soma += gastos[i]
        total[bairro] = soma
    return total