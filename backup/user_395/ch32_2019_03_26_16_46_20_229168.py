a = str(input('Você tem dúvidas?'))
while a != 'não':
    if a == 'nao':
        print ('Até a próxima')
    elif a != 'não':
        print ('Pratique mais')
        a = str(input('Você tem dúvidas?'))
        break