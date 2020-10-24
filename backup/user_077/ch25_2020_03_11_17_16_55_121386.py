import math
def d(v,θ):
    y=((v**2)*math.sin(2*θ))/9.8
    return y
a=input('Velocidade')
b=input('Ângulo')
a=int(a)
b=int(b)
z=float(d(a,b))
if z<98:
    print('Muito perto')
elif 98<=z<=102:
        print('Acertou!')
elif z>102:
        print('Muito longe')