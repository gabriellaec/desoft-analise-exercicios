def calcula_tempo(dnomes_aceleração):
    novodic={}
    V=[]
    tempo=[]
    for nome in dnomes_aceleração:
        i=0
        c=0
        while i < len(dnomes_aceleração) and c < len(V):
            tempo=(V[c])/a[i]
        novodic=dnomes_aceleração[nome[tempo]]
    return novodic 