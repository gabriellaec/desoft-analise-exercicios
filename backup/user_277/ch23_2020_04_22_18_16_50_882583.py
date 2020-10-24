vel=int(input("velocidade do carro: "))
if vel>80:
    print("voce foi multado")
    preco=(vel-80)*5
    print(preco)
else:
    print('Não foi multado')