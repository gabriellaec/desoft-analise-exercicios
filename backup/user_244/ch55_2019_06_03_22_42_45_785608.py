def verifica_primo(x):
    i = 2
    while i < x:
        if x%i == 0:
            return False
        
        i += 1
    return True


def primos_entre(a, b): 
    lista = [a:b]
    lista_primos = []
    
    
    
    for i in lista:
        if verifica_primo(i):
            lista_primos.append(lista[i])
            
    return lista_primos
        
        
        

        


            
               
        
     
    