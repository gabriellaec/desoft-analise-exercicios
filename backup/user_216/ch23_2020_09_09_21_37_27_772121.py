v = float(input("Velocidade"))

if v <= 80:
    print("Não foi multado")
else:
    print("{0:.2f}".format((v-80)*5))