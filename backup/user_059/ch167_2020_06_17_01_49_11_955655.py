def bairro_mais_custoso(d):
    x = total_do_semestre_por_bairro(d)
    valores = list(x.values())
    nomes = list(x.keys())
    y = 0
    j = 0
    for i in valores:
        if i > y:
            y = i
            j = valores.index(i)
    return nomes[j]
