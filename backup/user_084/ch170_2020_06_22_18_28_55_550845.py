def apaga_repetidos(STR):
    primeiros=[]
    g=STR
    for i in range(len(STR)):
        if not STR[i] in primeiros:
            primeiros.append(STR[i])
            g=STR
        if STR[i] in primeiros:
            g=STR.replace(STR[i],'*')
    return g
           
        
        