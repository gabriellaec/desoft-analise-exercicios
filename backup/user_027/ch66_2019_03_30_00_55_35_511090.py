def capitaliza(x):
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	comeco = ALFABETO[alfabeto.find(x[0])]
	final = x[1:]
	return comeco + final