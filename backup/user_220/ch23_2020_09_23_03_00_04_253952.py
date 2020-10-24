velocidade = int(input('Qual a velociadade do carro? '))
def x(velocidade):
    if velocidade > 80 :
        y=(velocidade-80)*5
        return("Sua multa vale {0:.2f}".format(y))
    else:
        return("Não foi multado")
print(x(velocidade))

                            