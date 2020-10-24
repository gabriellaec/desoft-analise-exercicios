x = input('Qual a velocidade do carro?')
if x > 80:
    y = 5*x
    print('Você foi multado')
else x <=80:
    print('Não foi multado')
print('A multa é de {0:.2f}'.format(y))