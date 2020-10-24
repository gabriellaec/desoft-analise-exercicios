def ace_temp(aceleracao):
    temp = (200/aceleracao)**1/2
    return temp

def calcula_tempo(dic):
    dic_tempo = {}
    for nome, aceleracao in dic.items():
        tempo = ace_temp(aceleracao)
        dic_tempo[nome] = str(tempo)

    return dic_tempo