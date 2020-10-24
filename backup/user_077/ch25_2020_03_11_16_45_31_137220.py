import math
def d(v,θ):
    y=((v**2)*math.sin(2*θ))/9.8
    a=input('Velocidade')
    b=input('Ângulo')
    z=d(a,b)
    if z<98:
        print'Muito perto')
    else:
        if 98<=z<=102:
            print('Acertou!')
        else:
            if z>102:
            	print('Muito longe')