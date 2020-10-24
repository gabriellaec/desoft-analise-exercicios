def total_do_semestre_por_bairro (dic):
    dic2={}
    for bairro,lista in dic.items():
        novalista=[]
        for i in range (6,12):
            novalista.append (lista[i])
        gasto=sum (novalista)
        dic2[bairro]=gasto
    return dic2