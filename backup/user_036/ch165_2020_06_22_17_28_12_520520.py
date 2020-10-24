def mais_populoso(dict):
    maior, maior_nome = 0, ' '
    for k, v in dict.items():
        pop = 0
        for key, value in v.items():
            pop += value
        if pop > maior:
            maior = pop
            maior_nome = k
    return maior_nome