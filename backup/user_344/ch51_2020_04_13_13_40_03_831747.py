def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    elif numero % 2 == 0:
        return False
    n = 3 
    while n< numero:
        if numero % n == 0:
            return False
        n+=2
    return True

def primos_entre(a,b):
    if b> a:   
        lista=[0]*(b-a)
    lista[0]= a
    c=0
    e = 0 
    while e< len(lista):   
        lista[e] = a+c 
        e+=1
        c+=1
    
    i=0
    l=[]
    while i < len(lista):
        if eh_primo(lista[i]) == True:
            l.append(lista[i])
        i+=1
    return l