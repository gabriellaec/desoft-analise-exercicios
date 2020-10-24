x=input("qual a velocidade do carro?")
if x>80:
    print("você foi multado,em{}",round((x-80)*5),2)
else:
    print("Não foi multado")
    