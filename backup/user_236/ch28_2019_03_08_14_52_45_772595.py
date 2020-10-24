a=float(input(quantos km/h))
if a>80:
    b=(a-80)*5
    print("você foi multado em R$ {0:.2f}".format(b))
else:
    print("Não foi multado")
