velocidade = int(input('qual a velocidade do seu carro? '))
if velocidade > 80:
    print('ecebeu multa otario')
    print('pague '(velocidade-80)*5)
else:
    print('pode ir')