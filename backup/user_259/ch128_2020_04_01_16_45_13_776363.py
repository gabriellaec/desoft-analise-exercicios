movendo = input("Está se movendo?(n/s) ")
if movendo == 's':
    deveria_mover = input("Deveria se mover?(n/s) ")
    if deveria_mover == 's':
        print('Sem problemas!')
    elif deveria_mover == 'n':
        print('Silver tape')
    
elif movendo == 'n':
    deveria_parado = input("Deveria estar parado?(n/s)")
    if deveria_parado == 's':
        print('Sem problemas!')
    elif deveria_parado == 'n':
        print('WD-40')