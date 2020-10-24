def calcula_tempo(dicionario_de_atletas):
    dic_nome_tempo={}
    for nome in dicionario_de_atletas:
        tempo= (200/dicionario_de_atletas[nome])**(1/2)
        dic_nome_tempo[nome]=tempo
    return dic_nome_tempo
    