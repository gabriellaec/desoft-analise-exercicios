movimento = input('O objeto está se movendo? (S/N) ')

if movimento == 'S':
    deveria_se_mover = input('Deveria se mover? (S/N) ')
    if deveria_se_mover == 'S':
        print('Sem problemas!')
    else:
        print('Silver tape')        
else: #movimento == 'N'
    deveria_estar_parado = input('Deveria estar parado? (S/N) ')
    if deveria_estar_parado == 'S':
        print ('Sem problemas!')
    else:
        print ('WD-40')