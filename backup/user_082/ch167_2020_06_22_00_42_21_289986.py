def bairro_mais_custoso(empresa):
    novo_dic = {}
    maior_custo = 0
    bairo_custoso = ''
    for filial in empresa:
        novo_dic[filial] = 0

        for mes in empresa[filial][6:]:
            novo_dic[filial] += mes

        if novo_dic[filial] > maior_custo:
            maior_custo = novo_dic[filial]
            bairro_custoso = filial

    
    return bairro_custoso