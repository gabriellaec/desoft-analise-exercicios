def mais_populoso (dic):
    estado_mais_pop = " "
    maior = 0
    for estado, cidade in dic.items():
        população = 0
        for pop in cidade.values():
            população += pop
        if população > maior:
            estado_mais_pop = estado
            maior = população
    return estado_mais_pop