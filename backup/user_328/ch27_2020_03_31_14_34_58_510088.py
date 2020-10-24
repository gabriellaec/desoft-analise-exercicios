duvida= True 
a= input("Tem dúvida(s/n)? ")
if a == 'n':
    duvida= False 
    print ('Até a próxima')
while duvida == True:
    print('Pratique mais')
    a= input("Tem dúvida(s/n)? ")
    if a == 'n':
        duvida = False
        print('Até a próxima')
    break