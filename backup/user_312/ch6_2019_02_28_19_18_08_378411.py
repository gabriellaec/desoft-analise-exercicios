def encontra_maximo(lista):
    max=lista[0][0]
    eixox=len(lista)-1
    eixoy=len(lista[0])-1
    count=0
    count2=0
    while count<eixox:
        while count2<eixoy:
            if lista[count][count2]>max:
                max=lista[count][count2]
            count2+=1
        count+=1
    return max