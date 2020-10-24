def calcula_tempo(dicionario, velocidade, aceleracao):
    dicionario_com_tempo = {}
    for nomes in dicionario.keys():
        dicionario_com_tempo[nomes] = velocidade/aceleracao
    return dicionario_com_tempo