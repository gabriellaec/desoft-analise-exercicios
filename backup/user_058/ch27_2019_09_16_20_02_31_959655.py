def tempo(c,t):
	x= c*10*365*t # minutos
	y= x/(60*24)
	return y

c=int(input("quantos cigarros você fuma por dia? "))
t=int(input("Você fuma à quantos anos? "))
print(tempo(c,t))