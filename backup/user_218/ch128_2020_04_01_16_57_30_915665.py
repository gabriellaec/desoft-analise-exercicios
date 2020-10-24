a = input('O objeto está se movendo? (s/n)')
if a == 's':
    b = input('O objeto deveria se mover? (s/n)')
    if b == 's':
        print('Sem problemas!')
    if b == 'n':
        print('Silver tape')
if a == 'n':
    c = input('O objeto deveria estar parado? (s/n)')
    if c == 's':
        print('Sem problemas!')
    if c == 'n':
        print('WD-40') 