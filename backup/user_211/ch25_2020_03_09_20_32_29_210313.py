import math
def dist_da_jaca(v,a):
    d=((v**2)*(math.sin(math.radians(2*a)))/9.8)
    if d>102:
        print ('Muito longe')
    if d<98:
        print ('Muito perto')
    else:
        if d<102 and d>98:
            print( 'Acertou!')