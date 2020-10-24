def total_do_semestre_por_bairro(infra):
    total = {}
    for bairro, gastos in infra.items():
        soma = 0
        for i in range(6,12):
            soma += gastos[i]
        total[bairro] = soma
    return total

def bairro_mais_custoso(infra):
    total = total_do_semestre_por_bairro(infra)
    caro = ['',0]
    for bairro,gasto in total.items():
        if gasto > caro[1]:
            caro = [bairro,gasto]
    return caro[0]