def teste(n):
    primo=True
    i=2
    if n<=1:
        primo=False
    while i<n:
        if n%i==0:
            primo=False
        i+=1
    return primo

def lista_primos(n):#deu certo no spyder
    i=2
    c=01
    l=[]
    while c<=n:
        if teste(i): 
            c+=1 
            l.append(i)
        i+=1
    return l