import math
def d(v,θ):
    y=((v**2)*math.sin(2*θ))/9.8
    if y<98:
        print('Muito perto')
    else:
        if 98<=y<=102:
            print('Acertou!')
        else:
            if y>102:
            	print('Muito longe')