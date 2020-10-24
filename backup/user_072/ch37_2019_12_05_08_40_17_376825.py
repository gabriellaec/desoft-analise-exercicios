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

 
def lista_primos(z): 
    i=0
    lista=[] 
    while len(lista) < z+1:
        if eh_primo(i)==True:  			
                lista.append(i)	
        i+=1
    return lista