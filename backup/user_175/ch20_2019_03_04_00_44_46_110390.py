distancia = float(input())
if distancia <= 200:
    valor = distancia*(0.50)
    print (valor)
else:
    valor = (200*0.50) + ((distancia - 200)*(0.45))
    print(valor)
