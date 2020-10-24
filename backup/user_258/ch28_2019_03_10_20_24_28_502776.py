v=int(input('Qual a velocidade do carro? '))
if v>80:
    m=(v-80)*5
    print('Você foi multado em R$ {0}'.format(m))
else:
    print('Não foi multado')
    