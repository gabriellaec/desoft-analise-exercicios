def calcula_tempo(dicionario):
    dic2 = {}
    for i in dicionario:
        a = dicionario[i]
        conta  = (200/a)**(1/2)
        dic2[i] = conta
    return dic2
