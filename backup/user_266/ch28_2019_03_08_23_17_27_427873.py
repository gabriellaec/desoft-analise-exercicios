v = int(input('Velocidade: '))
if v > 80:
    p = (v-80)*5
    print('Você foi multado!')
    print('Valor da multa é de R${0},00'.format(p))
else:
    print('Não foi multado')