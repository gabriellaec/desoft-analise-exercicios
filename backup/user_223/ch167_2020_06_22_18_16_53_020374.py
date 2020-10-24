def bairro_mais_custoso(dicio):
    dic_total={}
    for bairro, gastos in dicio.items():
        gastos_totais = 0
        for mes in range (0, 11):
            gastos_totais += gastos[mes]
        dic_total[bairro] = gastos_totais

    oc = 0       
    for v in dic_total.values():
        if v>oc:
            oc = v
            
    for p,o in dic_total.items():
        if o == oc:
            return p
    return p