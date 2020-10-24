def MUV(a):
    #V**2 = vo**2 +2*a*ds
    vo = 0 
    V =(vo +2*a*100)**1/2
    #V = a*t
    t = V/a
    return t
    
def calcula_tempo(dicionario):
    dic = {}
    for e in dicionario:
        dic[e] = MUV(t)
    return dic
        

    