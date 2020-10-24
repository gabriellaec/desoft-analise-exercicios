def verifica_lista (lista):
    só_par = True
    só_impar = True
    for i in lista:
        if i%2!=0:
            só_par = False
        if i%2==0:
            só_impar = False
    if só_par==True and só_impar==False:
        return 'par'
    if só_par==False and só_impar==True:
        return 'ímpar'
    if só_par==False and só_impar==False:
        return 'misturado'