while True:
    esta_se_movendo = input('Esta se movendo? ')
    if esta_se_movendo == 'n':
        deveria_estar_parado = input('Deveria estar parado? ')
        if deveria_estar_parado == 'n':
            print('Use WD-40')
            break
        elif deveria_estar_parado == 's':
            print('Sem problemas!')
            break
    elif esta_se_movendo == 's':
        deveria_se_mover = input('Deveria se mover? ')
        if deveria_se_mover == 'n':
            print('Silver tape')
            break
        elif deveria_se_mover == 's':
            print('Sem problemas!')
            break