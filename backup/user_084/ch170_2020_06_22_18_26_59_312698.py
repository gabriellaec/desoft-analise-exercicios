def apaga_repetidos(STR):
    primeiros=[]
    g=STR
    for i in range(len(STR)):
        if STR[i] not in primeiros:
            primeiros.append(STR[i])
        elif STR[i] in primeiros:
            g=STR.replace(STR[i],'*')
    return g
           
        
        