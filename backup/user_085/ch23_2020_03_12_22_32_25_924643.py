a = float(input('Digite a velocidade do veículo: '))
if a<= 80:
    print('Não foi multado)')
else:
    b = ((a-80)*5.00)
    ff = '{:.2f}'.format(b)
    print(ff)