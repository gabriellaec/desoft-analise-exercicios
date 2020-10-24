def total_do_semestre_por_bairro(dic):
    gastos = dict()
    for bairro in dic:
        gastos[bairro] = 0
        for i in range(6,len(dic[bairro])):
            gastos[bairro] += dic[bairro][i]
    return gastos

def bairro_mais_custoso(gastos):
    maior_gasto = 0
    bairro_maior_gasto = 0
    for bairro in gastos:
        gasto_bairro = gastos[bairro]
        if gasto_bairro > maior_gasto:
            maior_gasto = gasto_bairro
            bairro_mairo_gasto = bairro
    return bairro_maior_gasto