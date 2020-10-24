esta_movendo = input('O objeto está se movendo?(s/n) ')
if esta_movendo == 's':
    deveria = input('O objeto deveria se mover?(s/n) ')
    if deveria == 's':
        print('Sem problemas!')
    if deveria == 'n':
        print('Silver tape')
        
if esta_movendo == 'n':
    deveria = input('O objeto deveria estar parado?(s/n) ')
    if deveria == 's':
        print ('Sem problemas!')
    if deveria == 'n':
        print ('WD-40')
        