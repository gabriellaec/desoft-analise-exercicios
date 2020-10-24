velocidade = int(input("Insira a velocidade "))
if velocidade > 80:
    m = (velocidade-80)*5
    print("você foi multado! em {0:.2f}".format(m))
else:
    print("Não foi multado")