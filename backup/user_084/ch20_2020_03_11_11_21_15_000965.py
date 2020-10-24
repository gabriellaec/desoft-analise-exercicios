x=int(input('distância da viagem: '))
if 0<x<200:
    P=0.50*x
    print('o valor da viagem é de R$ %5.2f' % P)
else:
    P=0.45*x
    print('o valor da viagem é de R$ %5.2f' % P)