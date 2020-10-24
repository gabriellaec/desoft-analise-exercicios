a = float(input('qual a distancia que voce quer percorrer?'))

if a >= 200:
    preco = a*0.45
else:
    preco = a*0.5
print('voce pagara {0:.2f}'.format(preco))