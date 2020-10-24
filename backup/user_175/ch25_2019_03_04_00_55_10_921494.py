dis = float(input('Informe a distância desejada: '))

if dis <= 200:
    valor = dis*(0.50)
    print(valor)
else:
    valor = 100 + ((dis - 200)*(0.45))
    print('{:.2f}' .format(valor))