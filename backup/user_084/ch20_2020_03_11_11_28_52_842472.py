x=int(input('distância da viagem: '))
if 0<x<200:
    P==200*0.50
    print('o valor da viagem é de R$ %5.2f' % P)
elif x>200:
    P==200*0.50+(x-200)*0,45
    print('o valor da viagem é de R$ %5.2f' % P)