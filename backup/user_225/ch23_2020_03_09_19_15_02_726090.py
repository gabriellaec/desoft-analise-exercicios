velocidade = float(input("Velocidade do usuário: "))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print (("O valor da multa é R$:.2f}".format(multa)