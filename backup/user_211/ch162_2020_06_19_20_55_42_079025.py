def verifica_lista(lista):
    listapar=[]
    listaimpar=[]
    for i in range(0,len(lista)):
        if lista[i]%2==0 and len(lista)!=0:
            listapar.append(lista[i])
        else:
            listaimpar.append(lista[i])
    if len(listapar)==len(lista):
        return 'par'
    elif len(listaimpar)==len(lista):
        return 'ímpar'
    else:
        return 'misturado'