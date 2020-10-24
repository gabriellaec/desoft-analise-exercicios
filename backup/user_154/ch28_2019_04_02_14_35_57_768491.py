velocidade = int(input("Speed"))

if velocidade > 80:
    print("Você foi multado em R${0.2f}".format((velocidade-80)*5))
else:
    print("Não foi multado")