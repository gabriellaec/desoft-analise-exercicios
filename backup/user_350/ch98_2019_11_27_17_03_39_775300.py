def bairro_mais_custoso(dic):
    dic_gastos = total_do_semestre_por_bairro(dic)
    maior = "bairro"
    for bairro in dic_gastos:
        if bairro[0] > maior:
            maior = bairro
    return maior 
        