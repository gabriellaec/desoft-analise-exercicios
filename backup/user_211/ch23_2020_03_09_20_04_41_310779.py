x=input("qual a velocidade do carro?")
r=(x-80)*5
if x>80:
    print("você foi multado,em {0:.2f}".format(r))
else:
    print("Não foi multado")
    