x=float(input("qual a velocidade do carro em Km?"))
if x>=80:
    y=5*(80-x)
    print("o usuário foi multado em {}".format(y))
else:
    print("'Não foi multado'")
