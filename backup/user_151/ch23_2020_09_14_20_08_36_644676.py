a = int(input('velocidade '))
if a <= 80:
    print('Não foi multado')
else:
    print(f'{(a-80)*5:.2f}'
