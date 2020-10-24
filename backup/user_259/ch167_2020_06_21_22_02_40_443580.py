def total_do_semestre_por_bairro(dic):
    gastos = dict()
    for bairro in dic:
        gastos[bairro] = 0
        for i in range(6,len(dic[bairro])):
            gastos[bairro] += dic[bairro][i]
    return gastos

def bairro_mais_custoso(dic):
    maior_gasto = 0
    bairro_maior_gasto = 0
    gastos = total_do_semestre_por_bairro(dic)
    for bairro in gastos:
        if gastos[bairro] > maior_gasto:
            maior_gasto = gastos[bairro]
            bairro_maior_gasto = bairro
    return bairro_maior_gasto
        
        
        