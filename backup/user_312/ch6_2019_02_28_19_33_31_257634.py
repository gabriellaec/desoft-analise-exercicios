lista=[[0,0,0]*3]*3
def encontra_maximo(lista):
    max=lista[0][0]
    eixox=len(lista)
    eixoy=len(lista[0])
    count=0
    count2=0
    print(eixox, eixoy)
    print(count, count2)
    while count<eixox:
        while count2<eixoy:
            if lista[count][count2]>max:
                max=lista[count][count2]
            print(count, count2)
            count2+=1
        count2=0
        count+=1
    return max