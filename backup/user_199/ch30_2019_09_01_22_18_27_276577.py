import math

v=float(input('qual a velocidade da sua jaca?'))
a=float(input('qual o angulo do lancamento da sua jaca?'))

def jacawar(v,a):
    d=v**2*math.sin(2*a)/9.8
    if 98<=d<=102:
        return 'Acertou!'
    elif 90<=d<=110:
        return 'Muito perto'
    else:
        return 'Muito longe'
    
print(jacawar(v,a))
              