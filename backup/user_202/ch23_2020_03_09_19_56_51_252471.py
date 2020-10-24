v = float(input("velocidade:"))
if v > 80:
    a = (v-80)*5
    print("{0:f.2}".format(a))
else:
    print('Não foi multado')