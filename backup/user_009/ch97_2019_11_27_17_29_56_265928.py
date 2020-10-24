def total_do_semestre_por_bairro(dic):
    ds = {}
    for k,v in dic.items():
        soma = 0
        g = v[6:12]
        for i in g:
            soma += float(i)
        ds[k] = soma
    return ds       
  