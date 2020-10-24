velocidade = int(input("Qual a velocidade? "))
if velocidade == 80:
    print("usuário foi multado")
if velocidade > 80:
    valor = velocidade - 80
    print("usuário foi multado")
    print("R${0}".format(valor))
else:
    print("Não foi multado")