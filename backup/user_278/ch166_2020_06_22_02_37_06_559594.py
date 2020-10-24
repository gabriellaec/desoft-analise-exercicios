def total_do_semestre_por_bairro(dicionario):
    #dic que retorna o gasto total com infraestrutura nos últimos 6 meses para cada bairro
    dic2 = {}
    for bairro, valores in dicionario.items():
        total = 0
        for valor in range(0,len(valores)):
            while valor < 6:
                total += valores[valor]
            dic2[bairro] = total
    return dic2