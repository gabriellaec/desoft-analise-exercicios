def bairro_mais_custoso(dicionario):
    dicionario_2 = total_do_semestre_por_bairro(dicionario)
    maior_valor = 0
    mais_caro = ''
    for chave, valor in dicionario_2.items():
        if valor > maior_valor:
            maior_valor = valor
            mais_caro = chave

    return mais_caro