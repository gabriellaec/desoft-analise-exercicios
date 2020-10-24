def calcula_tempo(dicioAtletas):
    AtletaETempo = {}
    vencedor = 0
    tempo = 0

    for atleta in dicioAtletas:
        aceleracao = dicioAtletas[atleta]
        TempoDeProva = (200/aceleracao)**0.5
        AtletaETempo[atleta] = TempoDeProva

    for atleta in AtletaETempo:
        if vencedor == 0:
            vencedor = atleta
            tempo = AtletaETempo[atleta]
        elif AtletaETempo[atleta] < tempo:
            vencedor = atleta
            tempo = AtletaETempo[atleta]
    
    return print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,tempo))