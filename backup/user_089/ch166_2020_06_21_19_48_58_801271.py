def total_do_semestre_por_bairro(dicionario):
    dic2 = {}
    for k,v in dicionario.items():
        soma = 0
        
        for e in v[6:]:
            soma += e
        dic2[k] = soma
    return dic2