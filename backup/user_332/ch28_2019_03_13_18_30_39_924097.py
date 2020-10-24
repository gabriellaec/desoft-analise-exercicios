def velocimetro (velocidade):
    if (velocidade < 80):
        multa = (velocidade - 80) * 5
        return(multa)
    else:
        return("Não foi multado")
velocidade = int(input("Sua Velocidade"))
print(velocimetro(velocidade))