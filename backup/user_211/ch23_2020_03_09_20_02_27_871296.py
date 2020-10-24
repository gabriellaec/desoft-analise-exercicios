x=input("qual a velocidade do carro?")
if x>80:
    print("você foi multado,em {0:.2f}", ((x-80)*5))
else:
    print("Não foi multado")
    