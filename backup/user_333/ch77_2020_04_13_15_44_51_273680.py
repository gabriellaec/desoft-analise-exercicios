import math

def calcula_tempo(dicionario):
    nome_tempo={}
    for nome_e_aceleracao in dicionario:
        nome=nome_e_aceleracao[0]
        aceleracao=nome_e_aceleracao[1]
        if aceleracao!='i' and aceleracoa!='o':
            tempo=aceleracao_tempo(float(aceleracao))
            nome_tempo[nome]=tempo
    return nome_tempo
        
def aceleracao_tempo(a):
    t=math.sqrt(200/a)
    return t
