objeto_movimento = str(input('O objeto esta movendo? '))
if objeto_movimento == 'sim':
    mov2 = str(input('Deveria se mover? '))
    if mov2 == 'sim':
        print('Sem problemas!')
    elif mov2 == 'nao':
        print('Silver tape')
    else:
        print('Reponda com sim ou nao')
elif objeto_movimento == 'nao':
    objeto_parado = str(input('Deveria estar parado?'))
    if objeto_parado == 'sim':
        print('Sem problemas!')
    elif objeto_parado == 'nao':
        print('WD-40')