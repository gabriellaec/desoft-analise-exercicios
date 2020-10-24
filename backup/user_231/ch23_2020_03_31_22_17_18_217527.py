v= int(input('qual a velocidade? '))
if v>80:
    m= (v-80)*5
    print('Voce foi multado')
    print(' a multa é de {:.2f}'.format(m))
else:
    print('não foi multado')
    