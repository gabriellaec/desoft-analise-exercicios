dis = float(input('Informe a distância desejada: '))

if dis <= 200:
    valor = distancia*(0.50)
    print(valor)
else:
    valor = 100 + ((distancia - 200)*(0.45))
    print(valor)