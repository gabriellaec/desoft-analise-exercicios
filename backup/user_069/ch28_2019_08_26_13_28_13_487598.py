v = float(input('Qual a velocidade? '))
if 80 >= v:
    print('Não foi multado')
elif v > 80:
    multa == (v-80)*5
    print('A multa foi de {0:.2f}'.format(multa))