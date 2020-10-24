def calcula_tempo(dicio):
    at = {}
    for k,v in dicio.items():
        at[k]=(200/v)**(1/2)
    return at
