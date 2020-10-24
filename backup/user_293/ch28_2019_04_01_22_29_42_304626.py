n= float(input("Qual a velocidade do carro?: "))
if n > 80:
    y= (n-80)*5
    print("O motorista foi multado em R${0:2f}".format(y))
else:
    print("O motorista não foi multado")