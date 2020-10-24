par=[]
impar=[]
def verifica_lista(lista_num):
    for i in range(len(lista_num)):
        if lista_num[i] % 2 == 0:
            par.append(lista_num[i])
        else:
            impar.append(lista_num[i])
    
    #if lista_num ==[]:
        #return 'misturado'    
    if len(par) == len(lista_num):
        return 'par'
    elif len(impar) == len(lista_num):
        return 'impar'
    if len(par) != len(lista_num) and len(impar)!= len(lista_num) :
        return 'misturado'
    print(par)