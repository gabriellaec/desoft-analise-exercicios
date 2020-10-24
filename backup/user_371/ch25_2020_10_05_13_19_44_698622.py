import math
def jaca(velocidade, angulo):
    d = (velocidade**2*math.sin(math.degrees(*2*angulo)))/9.8
    print (d)
    if d < 98:
        return 'Muito perto'
    elif d >= 98 and d <= 102:
        return 'Acertou!'
    else:
        return 'Muito longe'
print(jaca(int(input("Digite a velocidade ")),(int(input("Digite o angulo ")))))