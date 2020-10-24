def calcula_tempo(dic):
    dicionario = {}
    for nome,aceleracao in dic.itens():
        dicionario[nome] = ((200/ace)**(1/2))
    return dicionario