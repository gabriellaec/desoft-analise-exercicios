def multa(a):
    if a>80:
        z=(a-80)*5
        return("voce foi multado em {0:.2f}".format(z))
    else:
        return("Não foi multado")

a=float(input("qual sua velocidade?"))
print(multa(a))