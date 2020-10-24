p = float(input('Quantos quilômetros você percorreu? '))
x = 0.5*p
y = 100+(0.45)*(p-200)
if p<=200:
    print('Sua passagem custa R$ {0:.2f}'.format(x))
else:
    print('Sua passagem custa R$ {0:.2f}'.format(y))
        