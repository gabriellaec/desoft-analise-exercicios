from math import sin
vel=int(input("digite a vel: "))
ang=int(input("digite o angulo: "))
g=9.8
def calcula_jaca(vel,ang):
	d=((vel**2)*sin(2*ang))/g
	if d<=98:
		return "muito perto"
	elif d>=102:
		return "muito longe"
	else:
		return "acertou"
print(calcula_jaca(vel,ang))