n = int(input('Teste de numeros primos: '))
mult = 0

for cont in range(2, n):
	if n % cont == 0:
		print('Multiplo de', cont)
		mult += 1

if mult == 0:
	print('Numero Primo')\

else:
	(print('tem', mult, 'multipos acima de 2 e abaixo de', n))
	
    