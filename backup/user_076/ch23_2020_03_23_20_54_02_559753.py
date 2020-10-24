a=int(input("Qual a velocidade do carro?"))

if a>80:
    print ("Você foi multado.")
    valor = (a-80)*5
    print ("O valor da sua multa é de R${}".format("{0:.2f}".format(valor)))

else:
    print ("Não foi multado")