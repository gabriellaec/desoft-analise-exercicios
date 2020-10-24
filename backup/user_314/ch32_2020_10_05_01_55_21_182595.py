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
    
def lista_primos(n):  
  
    lista_p=[]
    i=0
  
    while(len(lista_p)<n):
        if(eh_primo(i)):
            lista_p.append(i)
        i+=1
  
    return lista_p
  