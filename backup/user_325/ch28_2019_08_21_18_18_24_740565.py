def velocidade(vel):
    if vel > 80:
        m = (vel - 80) * 5
        return("{0:.2f}".format((vel - 80) * 5))
    else:
        return("Não foi multado")
vel = int(input("digite a vel"))
print(velocidade(vel))