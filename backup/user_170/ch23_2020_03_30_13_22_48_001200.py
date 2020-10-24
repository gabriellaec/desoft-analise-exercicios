v = float(input('Qual a velocidade do carro: '))
if v > 80:
    m = (v-80)*5
    print('Multa: {0:.2f}' .format(m))
else:
    print('Não foi multado')