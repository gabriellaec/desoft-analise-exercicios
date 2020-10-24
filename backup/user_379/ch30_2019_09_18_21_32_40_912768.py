from math import sin,pi
vel=float(input("digite a vel: "))
ang=(float(input("digite o angulo: ")))*pi/180
g=9.8
def calcula_jaca(vel,ang):
	d=((vel**2)*sin(2*ang))/g
	if d<=98:
		return "Muito perto"
	elif d>=102:
		return "Muito longe"
	else:
		return "Acertou!"
print(calcula_jaca(vel,ang))