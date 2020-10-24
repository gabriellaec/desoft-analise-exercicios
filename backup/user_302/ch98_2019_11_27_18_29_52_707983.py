def bairro_mais_custoso(dicionario):
    valor = 0
    dic = total_do_semestre_por_bairro(dicionario)
    for i in dic():
        custo_bairro = dic[i]
        if custo_bairro > valor:
            custo_bairro = valor
            bairro_mais_custoso = i
    return bairro_mais_custoso