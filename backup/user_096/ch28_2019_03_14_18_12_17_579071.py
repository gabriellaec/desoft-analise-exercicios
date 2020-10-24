v=int(input('qual a velocidade:  '))
if v>80:
    m=(v-80)*5
    print('voce foi multado em {0:.2f}'.format(m))
else:
    print('Não foi multado')
