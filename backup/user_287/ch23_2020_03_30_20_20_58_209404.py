v = int(input('qual a velocidade:'))
multa = 0
if (v>80):
    multa = (v-80)*5.000
    print('multado')
    print('{0:.2f}'.format(multa))
else :
    print('nao foi multado')
  