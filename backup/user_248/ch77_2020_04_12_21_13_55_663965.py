def calcula_tempo(dicionario):
    dicionario2={}
    for i in dicionario:
        dicionario2[i]=(200/dicionario[i])**0.5
    return dicionario2
        
        