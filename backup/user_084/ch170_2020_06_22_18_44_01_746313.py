def apaga_repetidos(STR):
    primeiros=[]
    g=''
    for i in STR:
        if i.upper() not in primeiros:
            primeiros.append(i.upper())
            g+=i
        if i.upper() in primeiros:
            g+='*'
    return g
          

        