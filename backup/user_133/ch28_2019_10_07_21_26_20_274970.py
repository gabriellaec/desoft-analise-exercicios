velo = float(input('Digite a velocidade: '))

if velo > 80:
    multa = (velo - 80) * 5
    print ('Multado')
    print(f'{multa:.0.2f}')
else:
    print ('Nao foi multado')

    

    

