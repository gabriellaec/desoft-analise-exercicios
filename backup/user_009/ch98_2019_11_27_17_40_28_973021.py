a = total_do_semestre_por_bairro(dic_gastos)

def bairro_mais_custoso(a):
    l_gastos = []
    for bairro in a:
        l_gastos.append(a[bairro])
    mais_caro = max(l_gastos)
    for bairro in a:
        if a[bairro] == mais_caro:
            return bairro