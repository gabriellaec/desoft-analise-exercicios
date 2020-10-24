def aniversariantes_de_setembro(dic_datas):
    dic_final={}
    for k,v in dic_datas.items():
        if v[3:5]=="09":
            dic_final[k]=v
    return dic_final
            