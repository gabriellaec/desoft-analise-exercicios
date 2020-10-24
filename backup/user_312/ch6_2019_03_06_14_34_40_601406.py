import math
def encontra_maximo(lista):
    max=math.fabs(lista[0][0])
    count=0
    count2=0
    while count<len(lista):
        while count2<len(lista[0]):
            if math.fabs(lista[count][count2])>math.fabs(max):
                max=math.fabs(lista[count][count2])
            count2+=1
        count2=0
        count+=1
    return max