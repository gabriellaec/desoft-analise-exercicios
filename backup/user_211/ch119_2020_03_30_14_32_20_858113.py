import math
def calcula_euler(x,n):
    lista=[]
    lista.insert(0,1)
    lista.insert(1,x)
    i=2
    while(i<n):
        lista.insert(i,((x**(i+1))/(math.factorial(i))))
        i=i+1
    print(lista)
calcula_euler(2,3)