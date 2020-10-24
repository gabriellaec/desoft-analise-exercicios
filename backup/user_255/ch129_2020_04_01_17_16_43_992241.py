valor = int(input('Entre com um número, para saber o quadrado perfeito: '))
aux = 1

raizQ = int(valor ** (1/2))

if((raizQ ** 2) == valor ):
    print('O número {0} é um quadrado perfeito!!!'.format(int(valor)))
else:
    print('O número {0} não é quadrado perfeito!!!'.format(valor))