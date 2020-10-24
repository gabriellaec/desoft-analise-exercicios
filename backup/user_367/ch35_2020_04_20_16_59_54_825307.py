cont= True
while cont:
    lista=[]
    Q= int(input('Qual valor? '))
    if Q == 0:
        x= sum(lista)
        print(' A soma é: ')
        cont = False
    else:
        lista.append(Q)
        
        