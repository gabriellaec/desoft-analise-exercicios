def aniversariantes_de_setembro(dn):
    dic={}
    for i,n in dn.items():
        x=n[3]+n[4]
        if x=='09':
            dic[i]=n
    return dic
            