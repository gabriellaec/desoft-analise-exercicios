def retorna_conta():
    a = float(input("Qual foi o valor da sua conta do restaurante? "))
    a -= (a * 0.1)
    print( "Valor da conta com 10%: R${0:.2f}".format(a))