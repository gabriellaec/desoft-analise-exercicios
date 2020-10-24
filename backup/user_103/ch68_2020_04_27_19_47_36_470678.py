def separa_trios(lista):
    listan=[]
    for i in range(len(lista)):
        a=lista[i::3]
        listan.append(a)
        print (a)
    return listan
            