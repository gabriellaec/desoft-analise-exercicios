x = float (input ('Quantos km? '))
if x <= 200:
    y = 0.5 * x
    print ('O preço da passagem é: R${0:.2f}'.format(y))
else:
    y = 100 + (0.45 * (x - 200))
    print ('O preço da passagem é: R${0:.2f}'.format(y))