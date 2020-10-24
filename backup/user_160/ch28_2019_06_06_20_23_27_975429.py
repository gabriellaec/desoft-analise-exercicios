vel = int(input("Qual a velocidade do carro?"))
if vel > 80:
    print ("Você foi multado")
    multa = 5 * (vel - 80)
    print(multa)
    else:
        "Não foi multado"