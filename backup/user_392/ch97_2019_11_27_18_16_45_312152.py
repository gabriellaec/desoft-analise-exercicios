def total_do_semestre_por_bairro(x):
    maior  = 0
    for e,v in x.items():
        novo = sum(v[6:])
        if novo > maior:
            maior = novo
            return e