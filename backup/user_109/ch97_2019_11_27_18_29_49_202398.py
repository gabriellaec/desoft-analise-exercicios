def total_do_semestre_por_bairro (dicionario):
    soma = 0
    new_dict = {}

    for chave, valor in dicionario.items():
        for i in range(5):
            soma += valor[i]
            new_dict[chave] = soma

    return new_dict