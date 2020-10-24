def calcula_tempo(dic):
    final={}
    nomes=[]
    tempos=[]
    t=0
    i=0
    for x in dic.keys():
        nomes.append(x)
    for a in dic.values():
        t=10*(2**(1/2))/(a**(1/2))
        tempos.append(t)
    for y in nomes:
        final[y]=tempos[i]
        i=i+1
    return final