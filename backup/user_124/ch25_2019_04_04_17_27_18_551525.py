a = int(input("insira a distancia do destino em km: "))
if a <= 200:
    a = a*float(0.50)
    print("sua passagem será: R$ " + str(a))
else:
    a = a * float(0.45)
    print("sua passagem será: R$ " + str(a))