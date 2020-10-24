velocidade = int(input("Qual a velocidade? "))

if velocidade > 80:
    valor = velocidade - 80
    custo = valor * 5
    print("Multa: {0:.2f}".format(custo))

if velocidade <= 80:
        print("Não foi multado")