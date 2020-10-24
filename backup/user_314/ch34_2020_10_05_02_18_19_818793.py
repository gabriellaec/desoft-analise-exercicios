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

def maior_primo_menor_que(n):
    if(n<0):
        return -1
   
    else:
        
        i=0
        a=0
        while(i<n+1):
            
            if(eh_primo(i)):
                a=i
            i+=1
        
        return a             