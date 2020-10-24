def total_do_semestre_por_bairro(dicionario):
    dic = {}
    i = 0
    for keys,lista in dicionario.items():
        for numeros in lista:
            while i<=6:
                dic[keys] += numeros
            i += 1
    return dic