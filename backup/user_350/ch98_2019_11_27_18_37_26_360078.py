def bairro_mais_custoso(dic):
    dic_gastos = total_do_semestre_por_bairro(dic)
    maior = 0
    for k,v in dic_gastos.items():
        if v > maior:
            maior = bairro[0]
            return k
        