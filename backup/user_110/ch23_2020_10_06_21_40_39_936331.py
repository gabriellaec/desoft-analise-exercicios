def multa(v):
    return (v-80)*5

velocidade = int(input('qual a velocidade do seu carro? '))
if velocidade > 80:
    print('ecebeu multa otario')
    float(print('pague {0:.2f}'.format(multa))
else:
    print('Não foi multado')