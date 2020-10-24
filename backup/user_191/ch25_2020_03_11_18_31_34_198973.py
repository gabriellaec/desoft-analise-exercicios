import math
def jaca(v,t,g):
    g=t*180/math.pi
	d=v**2*math.sin(2*g)/9.8
	return d
if jaca(v,t,g)<102:
    if jaca(v,t,g)>98:
        print('Acertou!')
    else:
        print('Muito perto')
else:
    print('Muito longe')