vel=float(input('velocidade?'))
if vel>80:
    print ('Multa! Valor: R${0:.2f}'.format((vel-80)*5))
else:
    print ('Não foi multado')