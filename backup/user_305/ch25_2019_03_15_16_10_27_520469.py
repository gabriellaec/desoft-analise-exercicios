a = float(input('Quanto vc quer percorrer em km?'))
if a <= 200:
    b = (a * 0.50)
    print ('{0:.2f}'.format(b))
else:
    c = (200 * 0.50 + (a-200)*0.45)
    print ('{0:.2f}'.format(c))

    