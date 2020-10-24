v=int(input("Qual a velocidade do carro? "))

if v>80:
    print("Foi multado")
    valor=5*(v-80)
    print("O valor da multa foi de: R$ {0: .2f}".format(valor))
else:
    print("Não foi multado")