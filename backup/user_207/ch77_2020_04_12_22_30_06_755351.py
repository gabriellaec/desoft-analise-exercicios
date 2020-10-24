def calcula_tempo (atletas):
    new_dicio = {}
    for atleta, acel in atletas.items():
        t = (2*100/acel)**(0.5)
        new_dicio[atleta] = t
    

    return new_dicio