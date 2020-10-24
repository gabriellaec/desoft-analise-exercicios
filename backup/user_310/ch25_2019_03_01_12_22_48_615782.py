km=int(input("distancia: "))

if km <=200:
    preco= km*0.5
    print("{:.2f}".format(preco))
else:
    a= (km-200)*0.45
    preco= a+200*0.5
    print("{:.2f}".format(preco))
