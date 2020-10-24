def calcula_tempo(dicionario):
    novo_dicionario={}
    for nomes, aceleracao in dicionario.items():
        novo_dicionario[nomes]=(200/aceleracao)**0.5
    return novo_dicionario