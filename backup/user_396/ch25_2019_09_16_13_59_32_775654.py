x = int(input("Quantos km deseja percorrer? "))
if x <= 200:
    a = x * 0.5
    return a
else:
    a = 100 + (x-200)*0.45
	return a