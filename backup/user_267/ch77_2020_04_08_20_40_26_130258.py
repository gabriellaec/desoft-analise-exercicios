def calcula_tempo(dicio):
    nome_tempo = {}
    i = 0
    for e,a in dicio.items():
        t = (200/a)**(1/2)
        nome_tempo[e] = t
        i += 1
    return nome_tempo
    
    