def mais_populoso(dicionario):
    new_dict = {}
    soma = 0
    maior_soma = 0
    for chave in dicionario.keys:
        for chave2, valor2 in dicionario[chave].items():
            soma += valor2

        new_dict[chave] = soma

    maior_populacao = ''
    for chave3, valor3 in new_dict.items():
        if valor3 > maior_soma:
            maior_soma = valor3
            maior_populacao = chave3

    return maior_populacao