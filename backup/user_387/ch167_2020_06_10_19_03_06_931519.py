def total_do_semestre_por_bairro(dic):
    dic_novo = {}
    for bairro in dic:
        dic_novo[bairro] = []
        for i in range(5,12):
            dic_novo[bairro].append(dic[bairro][i])
    return dic_novo

def bairro_mais_custoso(dic):
    dic_novo = total_do_semestre_por_bairro(dic)
    dic_custo = {}
    for bairro in dic_novo:
        dic_custo[bairro] = 0
        for mes in dic_novo[bairro]:
            dic_custo[bairro] += mes
    
    mais_cust = ''
    cust = 0
    for bairro in dic_custo:
        if dic_custo[bairro] > cust:
            cust = dic_custo[bairro]
            mais_cust = bairro

    return mais_cust