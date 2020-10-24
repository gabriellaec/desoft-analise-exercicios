controle= True
contagem= 0
b= 1
conta= 1
while controle:
    if contagem < 99:
        b*= (1/2)
        w= conta + b
        resultado= conta + b
    elif contagem == 99:
        controle= False
        print (resultado)
    contagem += 1