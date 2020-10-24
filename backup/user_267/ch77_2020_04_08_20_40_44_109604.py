def calcula_tempo(dicio):
    nome_tempo = {}
    for e,a in dicio.items():
        t = (200/a)**(1/2)
        nome_tempo[e] = t
    return nome_tempo
    
    