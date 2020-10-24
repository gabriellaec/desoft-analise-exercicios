x=float(input("Escreva o total de dias: "))
y=float(input("Escreva o total de horas: "))
z=float(input("Escreva o total de minutos: "))
w=float(input("Escreva o total de segundos: "))

def calcula_segundos(x,y,z,w):
	t=(x*24*60*60)+(y*60*60)+(z*60)+w
	return t
print(calcula_segundos(x,y,z,w))