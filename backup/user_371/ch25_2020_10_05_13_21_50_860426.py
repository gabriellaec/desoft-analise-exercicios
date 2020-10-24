import math
def jaca(velocidade, angulo):
    d = (velocidade**2*math.sin(math.radians(2*angulo)))/9.8
    if d < 98:
        return 'Muito perto'
    elif d >= 98 and d <= 102:
        return 'Acertou!'
    else:
        return 'Muito longe'
print(jaca(float(input("Digite a velocidade ")),(float(input("Digite o angulo ")))))