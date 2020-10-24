def eh_primo(x):
    i= 3
    if x < 0:
        return False
    if(x==2):
        return True
    elif(x==1):
        return False
    elif(x==0):
        return False
    elif(x==3):
        return True    
    elif(x%2==0):
        return False    
    while(x > i):
        if(x%i==0):
            return False
        i= i + 2        
    return True

def primos_entre(a,b):
    lista_primos_entre= []
    i= a
    while a <= i <= b:
        if eh_primo(i)== True:
            lista_primos_entre.append(i)
        i= i + 1
    return lista_primos_entre