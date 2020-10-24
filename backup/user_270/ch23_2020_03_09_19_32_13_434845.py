velo = int(input("Qual a velocidade do carro do usuário"))
if velo > 80 :
    a = (velo-80)*5
    print(" Você foi multado! Sua multa foi de {0:.2f}.".format(a))
else:
    print("Não foi multado")
