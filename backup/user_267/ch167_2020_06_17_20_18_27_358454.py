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
maior = 0
a = 0
def bairro_mais_custoso(gasto_total):
    if gasto_total[a] > maior:
        maior = gasto_total[a]
        a += 1
    else:
        a += 1
    return 
    