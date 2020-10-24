def medias_por_inicial(dic):
    dn={}
    for i,n in dic.items():
        if i[0] not in dn:
            dn[i[0]]=n
        else:
            for h,j in dn.items():
                if i[0]==h:
                    dn[h]=(j+n)/2
    return dn