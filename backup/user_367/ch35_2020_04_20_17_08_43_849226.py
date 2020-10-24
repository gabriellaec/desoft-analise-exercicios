cont= True
while cont:
    Q= int(input('Qual valor? '))
    lista=[]
    if Q != 0:
        lista.append(Q)
    else:
        x= sum(lista)
        print(' A soma é: {0}' .format(x))
        cont = False
       
        
        