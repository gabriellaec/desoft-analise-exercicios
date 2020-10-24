x = int (input ('Quantos km? '))
if x <= 200:
    y = 0.5 * x
    print ('{0:.2f}'.format(y))
else:
    y = (0.5 * x) + (0.45 * (x - 200))
    print ('{0:.2f}'.format(y))