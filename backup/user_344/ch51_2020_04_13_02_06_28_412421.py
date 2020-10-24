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
    lista=[0]*(b-a)
    i=0
    l=[]
    while i < len(lista):
        lista[i] = a+1
        i+=1
        a+=1
        if eh_primo(lista[i]) == True:
            l.append(lista[i])
    return l
   
        
    
    