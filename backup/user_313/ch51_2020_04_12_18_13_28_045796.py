def eh_primo(x):
    if(x == 0 or x == 1 or x == -1):
        return(False)
    if (x == 2 or x == -2):
        return(True)
    if (x%2 == 0):
        return(False)
    
    a = 3
    while a < x:
        if x%a ==0:
            return(False)
        else:
            a = a + 2
    return(True)

lista = []
def primos_entre(a,b):
    if a < b:
        
        conta = a
    
    else:
        
        conta = b
    
    while True:
        
        if eh_primo(conta) == True:
            lista.append(conta)
            conta += 1
            if conta > b:
                
                break
        else:
            if conta >= b:
                
                break
            conta += 1
            continue
        
    if len(lista) == 0:
        return lista
    
    return lista

print(primos_entre(54,58))