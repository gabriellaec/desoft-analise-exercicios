par=[]
impar=[]
def verifica_lista(lista_num):
    print(lista_num)
    for i in range(len(lista_num)):
        if lista_num[i] % 2 == 0:
            par.append(lista_num[i])
  
        else:
            impar.append(lista_num[i])
        
    if len(par) == len(lista_num):
        return 'par'
    elif len(impar) == len(lista_num):
        return 'impar'
    elif lista_num ==[]:
        return 'misturado'
    else:
        return 'misturado'
