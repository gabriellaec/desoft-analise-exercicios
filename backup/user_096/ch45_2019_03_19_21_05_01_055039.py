def zera_negativos(listax):
    i=0
    while  i <len(listax):
        if listax[i]<0:
            listax[i]=0
        i+=1
    return listax
