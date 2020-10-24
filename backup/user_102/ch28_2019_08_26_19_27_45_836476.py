
km = float(input("Velocidade: "))


if km> 80:
    valor1 = (km-80)*5.00
    print('você foi multado por excesso de velocidade, o valor da multa é de R$ {0:.2f}'.format(valor1))
else:
    print('Não foi multado')
    
    