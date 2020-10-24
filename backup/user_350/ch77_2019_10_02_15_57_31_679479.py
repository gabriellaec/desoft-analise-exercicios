from math import sqrt
def calcula_tempo(dicatletas):
    for k,v in dicatletas:
        dicatletas[0]= sqrt((100/v)*2)
    return deic_nomes