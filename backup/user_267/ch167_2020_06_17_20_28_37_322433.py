def total_do_semestre_por_bairro(dicio_gastos):
    gasto_total = {}
    for bairro, lista in dicio_gastos.items():
        i = 6
        numero = 0
        while i < len(lista):
            numero += lista[i]
            i += 1
        gasto_total[bairro] = numero
    return gasto_total

def bairro_mais_custoso(gasto_total):
    maior = 0
    bairro_com_maior = 0
    for bairro, num in gasto_total.items():
        if num > maior:
        maior = num
        bairro_com_maior = bairro
    return bairro_com_maior
    