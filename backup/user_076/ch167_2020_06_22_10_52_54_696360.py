def bairro_mais_custoso (d):
    
    def total_do_semestre_por_bairro (d1):
        d2 = {}
        for bairro in d1:
            lista = d1[bairro]
            d2[bairro] = lista[6]+lista[7]+lista[8]+lista[9]+lista[10]+lista[11]
        return d2
    
    gastos_último_semestre = (total_do_semestre_por_bairro (d))
    
    for bairro in gastos_último_semestre:
        maior_gasto = 0
        if gastos_último_semestre[bairro] > maior_gasto:
            maior_gasto = gastos_último_semestre[bairro]
            bairro_mais_custoso = bairro
    
    return bairro_mais_custoso
    