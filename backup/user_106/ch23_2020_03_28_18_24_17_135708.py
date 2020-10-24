v=int(input('Qual a sua velocidade? '))

if v>80:
    multa=(v-80)*5
    print('Você foi multado, valor = {0:.2f}'.format(multa))
else:
    print('Não foi multado')