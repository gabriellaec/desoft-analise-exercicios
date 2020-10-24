def total_do_semestre_por_bairro (dic):
    
    dic_totais = {}
    for k, v in dic.items():
        total = 0
        lista = v
        for gasto in lista[6:]:
            total += gasto
            
        dic_totais[k] = total
        
    return dic_totais

def bairro_mais_custoso (dic_gastos):
    
    gastos = total_do_semestre_por_bairro (dic_gastos)
    maior_preco = 0
    bairro_caro = 0
    
    for bairro, total in gastos.items():
        if total > maior_preco:
            maior_preco = total
            bairro_caro = bairro
    
    return bairro_caro
    