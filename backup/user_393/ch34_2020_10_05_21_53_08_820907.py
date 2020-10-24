def eh_primo(x):
    i= 3
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

def maior_primo_menor_que(n):
    lista_primos_ate_n= []
    i= 0
    if n <= 2:
        return -1
    if eh_primo(n)== True:
        return n
    while i < n:
        if eh_primo(i)== True:
            lista_primos_ate_n.append(i)
        i= i + 1
    return max(lista_primos_ate_n)
    
    
    