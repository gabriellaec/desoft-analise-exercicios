def multas(velocidade):
    if velocidade>80:
        return "Você foi multado. Sua multa é de R${0:.1f}".format((velocidade-80)*5)
    else:
        return "Você andou na velocidade certa"

velocidade = float (input("Qual a velocidade do seu carro?: "))
print (multas(velocidade))