km=int(input("distancia: "))

if km <=200:
    preco= km*0.5
    return("{:.2f}".format(preco))
else:
    preco= km*0.45
    return("{:.2f}".format(preco))
       
