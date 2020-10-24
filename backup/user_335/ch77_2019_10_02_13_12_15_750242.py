def calcula_tempo(dicioAtletas):
    AtletaETempo = {}
    for atleta in dicioAtletas:
        aceleracao = dicioAtletas[atleta]
        TempoDeProva = (200/aceleracao)**0.5
        AtletaETempo[atleta] = TempoDeProva
    return AtletaETempo