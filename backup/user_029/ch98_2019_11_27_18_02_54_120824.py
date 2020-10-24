def bairro_mais_custoso(y):
    y = total_do_semestre_por_bairro(gasto)
    
    for k,v in y.items():
        maior = v[0]
        if v > maior:
            maior = v
    return k,maior