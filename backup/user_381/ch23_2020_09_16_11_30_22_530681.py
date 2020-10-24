x = int(input('Qual a velocidade do carro?'))
if x > 80:
    y = 5*x
    print('Você foi multado')
elif x <=80: 
    y = print('Não foi multado')
print('A multa é de {0:.2f}'.format(y))