vel=int(input("Qual a sua velocidade em km/h?"))
if vel>80:
    print("Valor da multa é R$ {0:.2f}".format(vel-80)*5)
else:
    print("Não foi multado")