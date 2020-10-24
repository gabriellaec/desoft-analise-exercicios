def calcula_tempo(dicio):
    for atleta,a in dicio.items():
        dicio[atleta] = (200/a)**0.5
    return dicio