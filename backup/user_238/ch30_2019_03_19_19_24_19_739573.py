import math
def jaca(v,o):
        d=(v**2*math.sin(2*o))/9.8
        if d<98:
            resposta='sua jaca esta muito perto'
        elif d>102:
            resposta='sua jaca esta muito longe'
        else:
            resposta='Parabens, sua jaca acertou o alvo!'
        return resposta
v=int(input('qual a velocidade da sua jaca? '))
o=int(input('qual o angulo da sua jaca? '))

print(jaca(v,o))
    