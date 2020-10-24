def multa(velocidade):
    if velocidade > 80:
        m = (velocidade-80)*5
        return "Foi multado em: {0}".format(m)
    else:
        return 'Não foi multado'
print(multa(int(input("Qual a sua velocidade: "))))