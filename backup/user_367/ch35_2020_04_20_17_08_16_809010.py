cont= True
while cont:
    Q= int(input('Qual valor? '))
    if Q != 0:
        lista=[]
        lista.append(Q)
    else:
        x= sum(lista)
        print(' A soma é: {0}' .format(x))
        cont = False
       
        
        