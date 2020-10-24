cont= True
while cont:
    Q= (input('Qual valor? '))
    lista=[]
    if Q != 0:
        lista.append(Q)
    else:
        x= sum(Q)
        print(' A soma é: {0}' .format(x))
        cont = False
       
        
        