def ace_temp(aceleracao):
    temp = (200/aceleracao)**1/2
    return temp

def calcula_tempo(dic):
    dic_tempo = {}
    for nome, aceleracao in dic.values():
        tempo = ace_temp(float(aceleracao))
        dic_tempo[nome] = tempo

    return dic_tempo