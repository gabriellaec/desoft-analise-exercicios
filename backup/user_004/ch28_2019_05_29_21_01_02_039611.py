v=int(input('Qual sua velocidade? '))

if v > 80:
    multa=(v-80)*5
    print('Você foi multado em {:.2f} reais!'.format(multa))
else:
    print('Você não foi multado')
    
  