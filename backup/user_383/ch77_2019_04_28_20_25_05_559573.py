def calcula_tempo(dicionario):
    dic={}

    for k,v in dicionario.items():
        tempo = (200/dicionario[k])**(1/2)
        dic[k] = tempo
    return dic
