def calcula_tempo(dnomes_aceleração):
    novodic={}
    V=[]
    tempo=[]
    for a in dnomes_aceleração:
        c=0
        while c < len(V):
            tempo.append((V[c])/dnomes_aceleração[a])
            c+=1
        novodic[a]=tempo
    return novodic 