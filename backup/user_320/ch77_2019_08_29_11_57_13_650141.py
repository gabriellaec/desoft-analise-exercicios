def calcula_tempo(dic):
    tempo = {chave: (100/(valor * 2))**0.5 for chave, valor in dic.items()}
    return tempo