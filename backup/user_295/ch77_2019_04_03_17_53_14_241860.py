import math 

def calcula_tempo (dic):
    for atleta, a in dic .items():
        tempo = math.sqrt (200/a)
        dic [atleta] = tempo
    return dic 