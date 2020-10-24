import math
i=0
lista[0]*n
lista[0]=1
lista[1]=x   
def calcula_euler(lista):
    while i<n:
        lista[i+1]=lista[i]*x/i
        i+=1
        soma=sum(lista)
        return soma
        
    
    