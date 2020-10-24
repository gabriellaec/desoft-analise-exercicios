lista=[-3,-4,-2,-5,-1,0,1,2,3,4]
t=0
def zera_negativos(lista):
    while lista[t] <= 0:
        lista[t]=0
        t+=1
    