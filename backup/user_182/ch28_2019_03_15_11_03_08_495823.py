v=int(input("qual a velocidade do seu carro"))
a=80
if v > a:
    p=(v-80)*5
    print("voce foi multado em {0:.2f}".format(p))
else:
    print("Não foi multado")