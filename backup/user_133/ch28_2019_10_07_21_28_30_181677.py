velo = float(input('Digite a velocidade: '))

if velo > 80:
    multa = (velo - 80) * 5
    print (f'Voce foi multado R${multa:.02f}')
else:
    print ('Nao foi multado')

    

    

