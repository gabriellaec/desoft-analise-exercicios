def eh_primo(n):   #Função teste para npumeros primos
    i=1
    c=0
    while(i<n):
        if(n%i==0):
            c+=1
        i+=1
    
    if(c!=1):
        return False
    else:
        return True

def primos_entre(a,b):
    i=a
    c=0   #contador de primos
    while(i<b+1):
        if(eh_primo==True):
            c+=1
        i+=1
    return c