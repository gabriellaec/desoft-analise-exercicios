v = float(input("Qual a velocidade?"))

if float(v > 80):
    a = float( (v-80)*5)
    print("Foi multado")
    print("Multa: {0:.2f}".format(a))

if float (v <= 80):
    print("Não foi multado")

