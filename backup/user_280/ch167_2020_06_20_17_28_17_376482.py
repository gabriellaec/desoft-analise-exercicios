def bairro_mais_custoso(dicio_ano):
    dicio = total_do_semestre_por_bairro(dicio_ano)
    maior = 0
    mais_pop = ''
    for bairro, soma in dicio.items():
        if soma > maior:
            maior = soma
            mais_pop = bairro
    return mais_pop
            
    