distancia = float(input("insira a distancia da viagem: "))

if distancia <= 200:
    preco = distancia * 0.5
    print("sua passagem será: {0:.2}R$" .format(preco))
else:
    preco = distancia * 0.45
    print("sua passagem será: {0:.2}R$" .format(preco))