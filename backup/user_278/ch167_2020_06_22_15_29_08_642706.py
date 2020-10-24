def bairro_mais_custoso(dicionario):
    dic2 = {}
    for bairro in dicionario:
        dic2[bairro] = 0
        for valor in dicionario[bairro][6:]:
            dic2[bairro]+=valor
    mais_custoso = ''
    maior_custo = 0
    for bairro, custo in dic2.items():
        if custo > maior_custo:
            maior_custo = custo
            mais_custoso = bairro
    return mais_custoso