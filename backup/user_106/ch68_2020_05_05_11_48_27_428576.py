def separa_trios(lista):
    trios=[]
    sala=[]
    for i in lista:
        if len(trios)<3:
            trios.append(i)
        else:
            sala.append(trios)
            trios=[i]
    sala.append(trios)
    return sala