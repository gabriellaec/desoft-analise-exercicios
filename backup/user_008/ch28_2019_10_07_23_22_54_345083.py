v= float(input("velocidade carro"))

if v > 80:
    x = (80-v)*5
    print ("foi multado à {0} reais".format(x))
else:
    print ("não foi multado")
    