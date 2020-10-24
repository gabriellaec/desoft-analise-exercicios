spd = float(input())
if spd > 80:
    multa = (spd - 80)*5
    print('o usuário foi multado')
    print('{.:2f}'.format(multa))
else:
	print('Não foi multado')