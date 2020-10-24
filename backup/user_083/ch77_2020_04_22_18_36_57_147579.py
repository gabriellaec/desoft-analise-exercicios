def calcula_tempo(dnomes_aceleração):
    novodic={}
    V=[]
    tempo=[]
    for a in dnomes_aceleração.values():
        i=0
        c=0
        while i < len(dnomes_aceleração) and c < len(V):
            tempo=(V[c])/a[i]
        novodic=nome[tempo]
    return novodic 