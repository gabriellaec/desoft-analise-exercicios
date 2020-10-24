def eh_primo(n):
    i=1
    contador=0

    while(n>=i):
        if(n%i==0):
            contador+=1;
        i+=1

    if(contador!=2):
        return False
    else:
        return True
    
def maior_primo_menor_que(n):
    if(n>0):
        i=0
        while(i<n+1):
            a=eh_primo(i)  
            i+=1
        
        return a     
   
    else:
        return -1