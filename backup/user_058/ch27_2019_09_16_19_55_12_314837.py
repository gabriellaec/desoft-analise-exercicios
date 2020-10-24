c=float(input("quantos cigarros você fuma por dia? "))
t=float(input("Você fuma à quantos anos? "))

def tempo(c,t):
	x= c*(t*12*30)
	y= x*(10/60/24) 
	return y
print(tempo(c,t))