v = int(input('Qual a velocidade do carro?'))
if v > 80:
    print(format((v - 80) * 5, '.2f'))
else:
    print('Não foi multado')