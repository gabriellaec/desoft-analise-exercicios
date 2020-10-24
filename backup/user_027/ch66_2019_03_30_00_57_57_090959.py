def capitaliza(x):
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x[0] in alfabeto:
        comeco = ALFABETO[alfabeto.find(x[0])]
        final = x[1:]
    elif x[0] in ALFABETO:
        comeco = alfabeto[ALFABETO.find(x[0])]
        final = x[1:]
	return comeco + final