def apaga_repetidos(STR):
    primeiros=[]
    for i in range(len(STR)):
        if STR[i] not in primeiros:
            primeiros.append(STR[i])
        elif STR[i] in primeiros:
            g=STR.replace(SRT[i],'*')
    return g
           
        
        