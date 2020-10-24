def meses(gasto):
    novo_dic={}
    for k,v in gasto.items():
        novo_dic[k]=v[6]+v[7]+v[8]+v[9]+v[10]+v[11]
    return novo_dic