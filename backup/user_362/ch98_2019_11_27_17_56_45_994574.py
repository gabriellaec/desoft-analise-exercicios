def bairro_mais_custoso(custo_1semestre):
    mais_custoso=0
    for bairro,total in custo_1semestre.items():
        if total>mais_custoso:
            maior = bairro
            mais_custoso = total
    return maior

#print (bairro_mais_custoso(total_do_semestre_por_bairro(dic)))