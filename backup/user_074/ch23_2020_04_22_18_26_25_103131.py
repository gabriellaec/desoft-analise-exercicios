vel=float(input('velocidade em km'))
if vel>80:
    valor=(vel-80)*5.00
    valor={":.2f"}.format(valor)
    print('multa de R${}'.format(valor))
else:
    print('Não foi multado')
    