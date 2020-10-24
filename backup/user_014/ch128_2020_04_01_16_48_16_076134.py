movimento = input('O objeto está se movendo? (Sim/Não) ')

if movimento == 'Sim':
    deveria_se_mover = input('Deveria se mover? (Sim/Não) ')
    if deveria_se_mover == 'Sim':
        print('Sem problemas!')
    else:
        print('Silver tape!')
        
else:
    deveria_estar_parado = input('Deveria estar parado? (Sim/Não) ')
    if deveria_estar_parado == 'Sim':
        print ('Sem problemas!')
    else:
        print ('WD-40!')
               