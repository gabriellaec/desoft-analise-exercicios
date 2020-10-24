def aceleração(t):
    a = 200/t**2
    return a

def calcula_tempo(dicionario):
    aceleracoes = {}
    for atletas in dicionario:
        t = dicionario[atletas]
        a = aceleração(t)
        aceleracoes[atletas] = a
    return aceleracoes