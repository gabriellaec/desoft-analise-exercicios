distanciafaixa1=200
tarifafaixa1=0.5
tarifafaixa2=0.45
distancia=float(input("qual a distância desejada?"))
if distancia<=distanciafaixa1:
    passagem=distancia*tarifafaixa1
else:
    passagem=(distanciafaixa1*tarifafaixa1)+(distancia-distanciafaixa1)*tarifafaixa2
print("%.2f" %passagem)
    
    