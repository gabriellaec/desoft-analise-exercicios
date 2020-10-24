
a=int(input("qual a velocidade do seu carro?: "))
if a<=80:
    print("não foi multado")
elif a>80:
    x=(a-80)*5
    print((" você teve uma multa de {0:.2f}").format(x))