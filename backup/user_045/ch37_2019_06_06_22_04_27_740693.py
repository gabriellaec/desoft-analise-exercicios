
def lista_primos(n):#deu certo no spyder
    i=2
    c=1
    l=[]
    while c<=n:
        if teste(i): 
            c+=1 
            l.append(i)
        i+=1
    return l
