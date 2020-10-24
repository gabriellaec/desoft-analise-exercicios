v = int(input('A qual velocidade você estava dirigindo?: '))
if v > 80:
    multa = ((v-80)*5)
    print('Você foi multado em R${0:.2f}!'.format(multa))
else:
    print('Não foi multado')