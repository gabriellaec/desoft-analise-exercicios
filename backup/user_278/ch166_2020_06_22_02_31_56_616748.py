def total_do_semestre_por_bairro(dicionario):
    #dic que retorna o gasto total com infraestrutura nos últimos 6 meses para cada bairro
    dic2 = {}
    for bairro, valores in dicionario.items():
        for valor in valores.values():
            total = 0
            while valor < 7:
                total += valor
        dic2[bairro] = total
    return dic2