c=float(input("quantos cigarros você fuma por dia? "))
t=float(input("Você fuma à quantos anos? "))

def tempo(c,t):
	x= c*(10/60/24)*(t*12*30)
	return x
print(tempo(c,t))