import math
pergunta1= float(input("Me diga a velocidade!"))
pergunta2= float(input("Me diga o ângulo"))

def jaca_war(v, x):
    xr= math.radians(x)
    distancia= ((v**2)*(math.sin(2*xr))/9.8
        if distancia>=98 and distancia<= 100:
            print ('Acertou!')
        elif distancia<98:
            print ('Muito longe')
        else:
            print ('Muito perto')
jaca_war(pergunta1, pergunta2)