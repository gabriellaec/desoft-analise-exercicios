def total_do_semestre_por_bairro(dic):
    gastos6={}
    for k,v in dic.items():
        gastos6[k]=sum(v[6:12:1])

    return(gastos6)
   
