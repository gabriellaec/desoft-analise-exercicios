def calcula_tempo(dicionario_de_atletas):
    dic_nome_tempo={}
    for nome in dicionario_de_atletas:
        tempo= (200**(1/2))/dicionario_de_atletas[nome]
        dic_nome_tempo[nome]=tempo
    print (dic_nome_tempo)
    