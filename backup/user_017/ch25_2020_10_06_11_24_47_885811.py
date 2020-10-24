import math
def jaca_war(v,x):
    xr=math.radians(x)
    d = ((v**2)*math.sin(2*x))/9.8
    dg=math.degrees(d)
    if d>=98 and d<=98:
        print('Acertou!')
    elif d<98:
        print("Muito perto")
    else:
        print("Muito longe")
        return d