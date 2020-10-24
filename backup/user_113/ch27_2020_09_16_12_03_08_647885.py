perg = input('Possui alguma dúvida?: ')

#x=True
while x==True :
    perg = input('Possui alguma dúvida?: ')
    if perg != 'não':
        print('Pratique mais')
    else:
        print('Até a próxima')
        x = False