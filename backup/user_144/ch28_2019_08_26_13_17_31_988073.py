vel = float(input(" Digite a velocidade do seu carro: "))
multa = vel - 80
excesso = (multa - 80) * 5
if vel < 80:
    print("Nào foi multado")
    
if vel >= 80:
    print('multado' + str(excesso))