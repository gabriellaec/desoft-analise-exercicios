velocidade = int(input("Qual a velocidade? "))
if velocidade == 80:
    print("usuário foi multado")
if velocidade > 80:
    valor = velocidade - 80
    print("R${0}".format(valor))
if valocidade < 80:
        print("Não foi multado")