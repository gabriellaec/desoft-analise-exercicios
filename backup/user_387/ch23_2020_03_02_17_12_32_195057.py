velocidade = float(input('d :'))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(round(multa, 2))

else:
    print('Não foi multado')
 