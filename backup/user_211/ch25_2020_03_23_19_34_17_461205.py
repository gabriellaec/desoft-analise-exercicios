import math
def dist_da_jaca(v,a):
    d=((v**2)*(math.sin(math.radians(2*a)))/9.8)
    if d>102:
        print ('Muito longe')
    elif d<98:
        print ('Muito perto')
    else:
        print('Acertou!')