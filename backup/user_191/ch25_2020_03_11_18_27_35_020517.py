import math
def jaca(v,t,g):
    g=t*180/math.pi
	d=v**2*math.sin(2*g)/9.8
    if d>98:
        if d<102:
            return 'Acertou!'
        else:
            return 'Muito longe'
    else:
        return 'Muito perto'