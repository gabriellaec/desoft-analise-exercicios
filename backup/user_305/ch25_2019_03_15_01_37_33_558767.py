a = int(input('Quanto vc quer percorrer em km?'))
if a <= 200:
    preco = (a * 0.50)
    print ('{0:.2f}'.format(preco))
else:
    print (a*0.45)

    