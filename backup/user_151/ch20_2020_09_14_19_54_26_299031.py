a = float(input('distancia '))
if a <= 200:
	print(round(0.5 * a, 2))
else:
	print(round(200 * 0.5 + 0.45*(a-200), 2))