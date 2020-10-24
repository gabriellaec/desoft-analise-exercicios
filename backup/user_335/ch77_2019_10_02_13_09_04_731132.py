def calcula_tempo(dicioAtletas):
    AtletaETempo = {}
    for atleta in dicioAtletas:
        TempoDeProva = (200/atleta[dicioAtletas])**0.5
        AtletaETempo[atleta] = TempoDeProva
    return AtletaETempo