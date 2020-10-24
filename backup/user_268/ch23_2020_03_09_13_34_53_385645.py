v=float(input('qual a velocidade?'))
if v>80:
    print('foi multado')
    m = (v-80) * 5
    print('R$ {0:.2f}'.format(m))
else:
    print( 'Não foi multado')