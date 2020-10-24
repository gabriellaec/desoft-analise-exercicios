def total_do_semestre_por_bairro(gastos):
    gasto_total = {}
    for bairro in gastos:
        gasto_total[bairro] = 0
        for mes in gastos[bairro][6:]:
            gasto_total[bairro] +=mes
    return gasto_total
def bairro_mais_custoso(lista):
    valor= []
    valor.append(0)
    nome= []
    nome.append(0)
    meses= total_do_semestre_por_bairro(lista)
    for i in meses:
        if meses[i] > valor[0]:
            valor[0] = meses[i]
            nome[0] = i
    return nome[0]