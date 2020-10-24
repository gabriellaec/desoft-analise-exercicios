def apaga_repetidos(STR):
    
    for i in range(len(STR)):
        primeiros=[]
        g=''
        if  STR[i] not in primeiros:
            primeiros.append(STR[i])
            g+=str(STR(i))
        if STR[i] in primeiros:
            g+='*'
    return g
          

        