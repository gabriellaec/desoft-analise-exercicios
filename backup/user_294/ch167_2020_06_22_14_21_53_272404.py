def bairro_mais_custoso(dic):
    novo_dic = {}
    for bairro in dic:
        novo_dic[bairro] = sum(dic[bairro][6:])
        
    mais_custoso = "a"
    maior_custo = 0
    for bairro in novo_dic:
        custo = novo_dic[bairro]
        if custo > maior_custo:
            maior_custo = custo
            mais_custoso = bairro
            
    return mais_custoso
