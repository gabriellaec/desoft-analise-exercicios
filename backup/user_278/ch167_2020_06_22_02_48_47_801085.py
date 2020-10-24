def bairro_mais_custoso(dic):
    #funçao do 166
    mais_custoso = ''
    maior_custo = 0
    for bairro, custo in dic2.items():
        if custo > maior_custo:
            maior_custo = custo
            mais_custoso = bairro
    return mais_custoso