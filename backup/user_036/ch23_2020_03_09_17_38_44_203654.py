v = float(input('Qual sua velocidade? '))
if v <= 80:
    print('Não foi multado.')
if v>80:
    print('Você foi multado em R$ {}'.format((v-80)*5))

input(v)