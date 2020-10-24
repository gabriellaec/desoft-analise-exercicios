def total_do_semestre_por_bairro(dic):
    gastos6={}
    for k,v in dic.items():
        gastos6[k]=sum(v[6:12:1])

    return(gastos6)
def bairro_mais_custoso(dic):
    novodic=total_do_semestre_por_bairro(dic)
    maiorv=0.0
    maiork='n'
    for k,v in novodic.items():
        if v > maiorv:
            maiorv = v
            maiork = k
    return maiork