def aniversariantes_de_setembro(dic_datas):
    dic_final={}
    for k,v in dic_datas.items():
        if v[4]=='9':
            dic_final[k]=v
    return dic_final
            