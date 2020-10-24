v = int(input("Velocidade"))
if v > 80:
    p = 5*(v-80)
    print("Voce foi multado em {0:.2f} reais".format(p))
else:
    print("Não foi multado")