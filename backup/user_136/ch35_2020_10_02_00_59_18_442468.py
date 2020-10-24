controle= True
soma= 0
while controle:
    numero= int(input('qual o numero? '))
    if numero== 0:
        controle= False
    else:
        soma+= numero
print (soma)