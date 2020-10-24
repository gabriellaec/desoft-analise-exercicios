a = float(input('distancia '))
if a <= 200:
	print(f'{(0.5 * a, 2):.2f}')
else:
	print(f'{(200 * 0.5 + 0.45*(a-200), 2):.2f}')