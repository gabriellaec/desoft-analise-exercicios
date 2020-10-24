m=input('Está se movendo?(n/s)')
if m=='s':
    d=input('Deveria se mover?(n/s)')
    if d=='s':
        print('Sem problemas!')
    elif d=='n':
        print('Silver tape')
elif m=='n':
    p=input('Deveria estar parado?(n/s)')
    if p=='s':
        print('Sem problemas!')
    elif p=='n':
        print('WD-40')