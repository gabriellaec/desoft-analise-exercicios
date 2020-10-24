def eh_primo(numero):   
    i=3
    if numero==0 or numero==1:       
        return False  
    if numero==2:
        return True 
    if numero%2==0: 
        return False 
    while numero>i:
        if numero%i==0:          
            return False       
        i+=2    
    return True 


def primos_entre(a,b): 
    i=a	
    primos = [] 
    while i<=b: 	
        if eh_primo(i)==True:  		
            primos.append(i)	
        i+=1
    return len(primos)
