pergunta= float(input("QUAL O VALOR DA CONTA DO RESTAURANTE?"))
print (pergunta)

valor_da_conta= float(pergunta - pergunta*10/100)
print("Valor da conta com 10%: R${0}".format (valor_da_conta))
