def bairro_mais_custoso(dicionario):
    maior = 0
    maior_custo = {}
    total_gastos = total_do_semestre_por_bairro(dicionario)
    for k,v in total_gastos.items():
        if v > maior:
            maior = v
            maior_custo = {k:maior}
    return maior_custo