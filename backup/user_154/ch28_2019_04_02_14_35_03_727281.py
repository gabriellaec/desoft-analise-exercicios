velocidade = int(input("Speed"))

if velocidade > 80:
    print("R${0}".format((velocidade-80)*5))
else:
    print("Não foi multado")