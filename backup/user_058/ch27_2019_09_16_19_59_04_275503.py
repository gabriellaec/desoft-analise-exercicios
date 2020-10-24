def tempo(c,t):
	x= c*(t*12*30)
	y= x*(10/60/24) 
	return y

c=int(input("quantos cigarros você fuma por dia? "))
t=int(input("Você fuma à quantos anos? "))
print(tempo(c,t))