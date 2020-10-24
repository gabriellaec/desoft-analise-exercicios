pergunta1=input('Está se movendo?  ')

if pergunta1=='n':
    pergunta2=input('deveria estar parado? ')
    if pergunta2=='s':
        print('Sem problemas!')
    elif pergunta2=='n':
        print('WD-40')
    
elif pergunta1=='s':
    pergunta3=input('deveria se mover? ')
    if pergunta3=='s':
        print('Sem problemas')
    elif pergunta3=='n':
        print('Silver tape')