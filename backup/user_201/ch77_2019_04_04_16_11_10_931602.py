def calcula_tempo(lista_atletas):
    dict_tempo={}
    for atleta,ac in lista_atletas.items():
        tempo=(200/ac)**0.5
        dict_tempo[atleta]=tempo
    return dict_tempo