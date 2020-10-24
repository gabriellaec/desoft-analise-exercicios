velocidade = int(input("Qual é a sua velocidade: "))
if (velocidade > 80):
    return ("Foi multado em R$ {0:.2f}".format((velocidade-80)*5))
else:
    return ("Não foi multado")
print (velocidade)