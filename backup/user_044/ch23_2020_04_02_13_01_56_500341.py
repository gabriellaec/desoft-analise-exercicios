vel=int(input("Qual a velocidade do seu carro? "))
if vel>80:
    print("Voce foi multado!")
    y=(vel-80)*5
    print("Multa de R${0:.2f}".format(y))
else:
    print('Não foi multado')
