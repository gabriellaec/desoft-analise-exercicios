import math
def calcula_tempo (atletas):
    #atletas chaves são strings e valores aceleração
    #devolver dicionario chaves nomes e valores tempo
    dicionario = {}
    for k,v in atletas.items():
        t = math.sqrt(200/v)
        dicionario[k] = t
    return dicionario