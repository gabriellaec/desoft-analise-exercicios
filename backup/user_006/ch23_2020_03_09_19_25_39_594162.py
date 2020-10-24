velocidade=input("Qual a velocidade do carro?")
if velocidade> 80:
    multa= float((velocidade-80)*5)
    print(multa)
else:
    print("Não foi multado")