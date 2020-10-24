def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for bairro,valores in dicionario.items():
        v = valores[6:]
        total = 0
        for x in v:
            total += x
        dic[bairro] = total
    return dic