v = float(input('Qual a velocidade do carro? '))
x = 5*(v-80)
if v<=80:
    print('Não foi multado')
else:
    print('Você foi multado em R${0:.2f}'.format(x))