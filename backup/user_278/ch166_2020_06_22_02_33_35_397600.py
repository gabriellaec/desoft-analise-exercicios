def total_do_semestre_por_bairro(dicionario):
    #dic que retorna o gasto total com infraestrutura nos últimos 6 meses para cada bairro
    dic2 = {}
    total = 0
    for bairro, valores in dicionario.items():
        for valor in valores.values():
            while valor < 7:
                total += valor
        dic2[bairro] = total
    return dic2