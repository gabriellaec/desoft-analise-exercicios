velocidade = float(input("Qual é a sua velocidade: "))
if (velocidade > 80):
    return ("Você foi multado")
    return ("Sua multa é de R$ {0:.2f}".format((velocidade-80)*5))
else:
    return ("Não foi multado")
