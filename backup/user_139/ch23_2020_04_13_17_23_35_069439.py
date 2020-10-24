x = int (input('Qual sua velocidade (km/h)? '))
if x > 80:
    y = (x - 80) * 5
    print ('A multa é de R${0:.2f}'.format(y))
else:
    print('Não foi multado')