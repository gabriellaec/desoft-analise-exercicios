import math

def encontra_maximo(matriz):
    i=0
    while i<3: 
        j=0
        while j<3:
            matriz[i][j]= int(math.fabs(matriz[i][j])) 
            j=j+1
        i=i+1
    maximo=matriz[0][0]
    i=0
    while i<3:
        j=0
        while j<3:
            if maximo<matriz[i][j]:
                maximo=matriz[i][j]
            j=j+1
        i=i+1
    return maximo