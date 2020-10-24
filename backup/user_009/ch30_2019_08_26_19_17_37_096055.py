from math import sin, degrees
v = float(input('v: '))
ao = float(input('ao: '))
pos = (v**2*sin(degrees(2*ao))/9.8)
if pos < 98:
    print('Muito perto')
elif pos >= 98 and pos <= 102:
	print('Acertou!')
else:
	print('Muito longe')
    

    