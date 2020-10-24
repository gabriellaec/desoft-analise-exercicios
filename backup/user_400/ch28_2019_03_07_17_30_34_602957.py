velocidade = int(input())
preço = (velocidade-80)*5
if velocidade > 80:
    print("Você foi multado")
    print("%.2f" % preço)