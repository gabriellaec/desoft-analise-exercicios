a = float(input('Qual a velocidade do carro?'))

if(a>80):
    print('Você foi multado')
    print('Multa')
    print(round(((5*(a-80))),2))

else:
    print('Não foi multado')