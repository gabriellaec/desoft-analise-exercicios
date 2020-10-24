velo = float(input('Escreva a sua velocidade:'))
if velo > 80:
    multa = 5*(velo - 80)
    print (multa)
    print ('Voce foi multado')
else:
    print ('Não foi multado')
