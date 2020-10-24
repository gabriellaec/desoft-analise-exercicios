vel=int(input("velocidade do carro: "))
if vel>80:
    print("voce foi multado")
    preco=(vel-80)*5.00
    print({0:.2f}.format(preco))
else:
    print('Não foi multado')