def jaca_wars (v, t):
    distancia= ((v**2)*(sin(2*t)))/9.8
        if distancia == 100:
            return 'Acertou!'
        if distancia > 100:
            return 'Muito longe'
        else:
            return 'Muito perto'
    