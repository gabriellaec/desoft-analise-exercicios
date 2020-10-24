def calcula_multa(velocidade):
    if (velocidade>80):
        return ("Você foi multado em R${0:.2f}".format((velocidade-80)*5))
    elif (velocidade<=80):
        return ("Não foi multado")

v = float(input("Informe a velocidade: "))

print(calcula_multa(v))