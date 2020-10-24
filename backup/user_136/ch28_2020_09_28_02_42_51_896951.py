controle= True
contagem= 0
b= 1/2
conta= 1 + 1/2
while controle:
    if contagem < 100:
        b*= (1/2)
        w= conta + b
        resultado= conta + b
    elif contagem == 100:
        controle= False
        print (resultado)
    contagem += 1