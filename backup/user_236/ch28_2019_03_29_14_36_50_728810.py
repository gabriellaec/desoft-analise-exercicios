a=float(input(quantos km/h))
if a>80:
    b=(a-80)*5
    print("Você foi multado")
    print ("R${0:.2f}".format(b))
else:
    print("Não foi multado")
