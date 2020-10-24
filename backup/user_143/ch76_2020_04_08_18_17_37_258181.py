def aniversariantes_de_setembro(d):
    dici={}
    for v,i in d.items():
        x=i[3]
        y=i[4]
        z=x+y
        if z=='09':
            dici[v]=i
    return dici
    