def calcula_tempo(dnomes_aceleração):
    novodic={}
    V=[]
    V_0=0
    tempo=[]
    for i in dnomes_aceleração.values():
        tempo=(V-V_0)/i
        novodic=nome[tempo]
    return novodic 