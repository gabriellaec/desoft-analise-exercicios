distanciafaixa1=200
tarifafaixa1=0.5
tarifafaixa2=0.45
distancia=float(input("qual a distância desejada?"))
passagem=0
if distancia<distanciafaixa1:
    passagem=distancia*tarifafaixa1
else:
    passagem=distancia*tarifafaixa2
    