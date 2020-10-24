def  calcula_tempo (d):
    dici={}
    for v,i in d.items():
        r=v
        t=(200/i)**(1/2)
        dici[r]=t
    return dici