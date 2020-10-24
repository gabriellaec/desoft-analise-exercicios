def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for keys,lista in dicionario.items():
        for numeros in lista[6:]:
            if keys in dic:
                dic[keys] += numeros
            else: 
                dic[keys] = numeros
    return dic
