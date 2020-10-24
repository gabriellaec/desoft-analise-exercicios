c=float(input("quantos cigarros você fuma por dia? ")
t=float(input("Você fuma à quantos anos? ")

def tempo(c,t):
	x= c*10*(t*12*30*24*60)
	y= x/60/24
	return y
print(tempo(c,t))