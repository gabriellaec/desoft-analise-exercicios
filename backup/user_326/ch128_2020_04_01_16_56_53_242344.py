objeto_esta_movendo = input('O objeto está se movendo? (n/s) ')
if objeto_esta_movendo == 's':
    deveria_mover = input('O objeto deveria estar se movendo? (n/s) ')
    if deveria_mover == 's':
        print('Sem problemas!')
    else:
        print('Silver tape')
else:
    deveria_ficar_parado = input('O objeto deveria estar parado? (n/s) ')
    if deveria_ficar_parado == 's':
        print('Sem problemas!')
    else:
        print('WD-40')