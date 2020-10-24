def calcula_tempo(dicionario_atletas):
    dicionario_tempo_final={}
    for i in dicionario_atletas:
        tempo = (100*2)/dicionario_atletas[i]
        dicionario_tempo_final[i]=tempo
    return dicionario_tempo_final