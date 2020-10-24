vel=int(input("velocidade do carro: "))
if vel>80:
    print("voce foi multado")
    preco=(vel-80)*5.00
    print(preco:.2f)
else:
    print('Não foi multado')