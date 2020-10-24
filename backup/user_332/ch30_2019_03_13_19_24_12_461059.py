import math
def jaca_wars (velocidade, angulo):
    d = (velocidade**2 * (2 * math.sin(angulo) * math.cos(angulo))/9.8)
    if (d < 99):
         return('Muito perto')
    elif (d > 101):
        return('Muito longe')
    else:
        return('Acertou!')
velocidade = int(input("Qual eh a velocidade?"))
angulo = int(input("Qual eh o angulo?"))
print(jaca_wars(velocidade, angulo))