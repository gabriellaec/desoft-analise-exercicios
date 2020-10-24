duvida = True
a = input("Tem dúvida? (sim/não)")
if a == 'não':
    duvida = False
    print ('Até a próxima')
while duvida == True:
    print ('Pratique mais')
    a2 = input("Tem dúvida? (sim/não)")
    if a2 == 'não':
        duvida = False
        print('Até a próxima')



