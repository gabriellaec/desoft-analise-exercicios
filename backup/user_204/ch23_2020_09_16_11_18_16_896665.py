velocidade = int(input("Qual a velocidade? "))
if velocidade >= 80:
    valor = velocidade - 80
    print("R${0:.f2}".format(valor))
if velocidade < 80:
        print("Não foi multado")