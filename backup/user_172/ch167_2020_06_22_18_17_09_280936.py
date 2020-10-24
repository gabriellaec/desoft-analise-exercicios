def bairro_mais_custoso(dic):
    bairros = {}
    for bairro,gastos in dic.items():
        x = 0
        semestre = 0
        for mes in range(6,12):
            semestre += gastos[mes]
        bairros[bairro] = semestre
        if semestre>x:
            maior = semestre
            bairromais = bairro
    return bairromais
        