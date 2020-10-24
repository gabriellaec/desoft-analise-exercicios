vel = float(input(" Digite a velocidade do seu carro: "))
multa = excesso - 80
excesso = 80 - multa * 5
if vel < 80:
    print("Nào foi multado")
    
if vel >= 80:
    print('multado' + str(excesso))