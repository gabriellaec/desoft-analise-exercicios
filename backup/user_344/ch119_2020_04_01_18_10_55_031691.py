def factorial (y):
    r =1 
    i=1
    while i<y:
        i+=1
        r*=i
    return r

def calcula_euler(x,n):
    i=0
    soma=0
    while i<n:
        soma+= (x**i)/factorial(i)
        i+=1
    return soma

        
