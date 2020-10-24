a = float(input('qual a distancia que voce quer percorrer?'))

if a > 200:
    preco = ((a-200)*0.45)+100
else:
    preco = 200*0.5
print('{0:.2f}'.format(preco))