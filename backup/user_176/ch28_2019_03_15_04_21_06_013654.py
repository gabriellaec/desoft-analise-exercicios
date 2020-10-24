v= int(input('qual a velocidade'))
if v>80:
    print ('a multa sera R$ {0:.2f}'.format(5*(v-80)))
else:
    print ('Não foi multado')