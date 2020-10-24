p1 = input("Está se movendo? (n/s)")
if p1=='n':
    p1 = input("Deveria estar parado? (n/s)")
    if p1=='n':
        print('WD-40')
    elif p1=='s':
        print('Sem problemas!')
elif p1 =='s':
    p1 = input("Deveria se mover? (n/s)")
    if p1=='n':
        print('Silver tape')
    elif p1=='s':
        print('Sem problemas!')