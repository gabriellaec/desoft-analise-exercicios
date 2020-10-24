x=int(input("qual a velocidade do carro?"))
r=(x-80)*5
if x>80:
    print("você foi multado,em {}", round(r,2))
else:
    print("Não foi multado")
    