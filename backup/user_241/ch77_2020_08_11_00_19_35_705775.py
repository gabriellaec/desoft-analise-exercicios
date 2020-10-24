def calcula_tempo(dicionario):
    nomes = list(dicionario.keys())
    dicionariot = {}
    for nome in nomes:
        t = 10/(dicionario[nome]/2)**1/2
        dicionariot[nome] = t
    return dicionariot
        