import math
def jaca_war(v,x):
    xr=math.radians(x)
    d = ((v**2)*math.sin(2*xr))/9.8
    if d>=98 and d<=102:
        print('Acertou!')
    elif d<98:
        print("Muito perto")
    else:
        print("Muito longe")
    return d