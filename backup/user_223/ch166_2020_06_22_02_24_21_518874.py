def total_do_semestre_por_bairro(dicio):
    dic_total={}
    for k, v in dicio.items():
        dic_total[k] = sum(v[k])
    return dic_total