import math
pergunta1= float(input("Me diga a velocidade!"))
pergunta2= float(input("Me diga o ângulo"))

def jaca_wars (v, t):
    xr= math.radians(t)
    distancia= ((v**2)*(math.sin(2*xr)))/9.8
        if distancia>=98 and distancia<= 100:
            return 'Acertou!'
        elif distancia<98:
            return 'Muito longe'
        else:
            return 'Muito perto'
    