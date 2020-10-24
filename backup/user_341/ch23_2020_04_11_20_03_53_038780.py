 vel = int(input("Qual a velocidade do carro?"))
if vel > 80:
    a = vel - 80
    multa = a * 5
    multac = round(multa, 2)
    print("Voce foi multado em:", multac)
else:
    print("Voce nao foi multado...")
    