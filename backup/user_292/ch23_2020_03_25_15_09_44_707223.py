v=float(input('qual a velocidade do carro?'))
if v>80:
    print('voce foi multado em R$ {0:.2f}'.format((v-80)*5))
else:
    print('Não foi multado')