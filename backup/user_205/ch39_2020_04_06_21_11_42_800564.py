def eh_par(x):
    if x%2==0:
        return True
def eh_impar(x):
    if x%2!=0:
        return True 
def collatz(x):
    lista = [0]*1000
    i = 0
    lista[0]=x
    while(lista<1001):
        if eh_par(i):
            lista[i+1]=lista[i]*3 +1 
        else:
            lista[i+1]=lista[i]/2      
    i +=1
    return x