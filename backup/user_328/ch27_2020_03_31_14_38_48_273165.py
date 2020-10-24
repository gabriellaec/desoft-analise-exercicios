duvida= True 
a= input("Tem dúvida(sim/não)? ")
if a == 'não':
    duvida= False 
    print ('Até a próxima')
while duvida == True:
    print('Pratique mais')
    a= input("Tem dúvida(sim/não)? ")
    if a == 'não':
        duvida = False
        print('Até a próxima')
    