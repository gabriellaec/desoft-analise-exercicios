def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for k, v in dicionario.items():
        i = 6
        while i<12:
            s = float(sum(v[i]))
            i += 1
        dic[k] = s
        
    return dic
            