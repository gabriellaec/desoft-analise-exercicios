x=float(input("qual a velocidade do carro em Km?"))
if x>80:
    y=5*(80-x)
    print("o usuário foi multado em %2f"% y)
else:
    print("'Não foi multado'")
