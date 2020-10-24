def multas (velocidade):
    if velocidade>80:
        return "Você foi multado. Sua multa é de R${0}".format((velocidade-80)*5)
    else:
        return "Você não foi multado"

velocidade = float (input("Qual a velocidade do seu carro?: km/h"))
print (multas(velocidade))