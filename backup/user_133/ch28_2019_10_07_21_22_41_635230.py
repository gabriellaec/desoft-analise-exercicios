velo = float(input('Digite a velocidade: '))

if velo <= 80:
    print ('Nao foi multado')
else:
    print ('Multado')
    multa = (velo - 80) * 5
    
print(f'{multa:.0.2f}')
    

