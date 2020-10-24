def total_do_semestre_por_bairro(x):
    total = dict()
    for bairro, gasto in x.items():
        f = sum(x[bairro][6:])
        total[bairro] = f
    return total

def bairro_mais_custoso(y):
    custo = dict()
    soma = total_do_semestre_por_bairro(y)
    s = 0
    pop = ''
    for bairro, gasto in soma.items():
        if f > s:
            s = f
            pop = bairro
    return pop
            
        