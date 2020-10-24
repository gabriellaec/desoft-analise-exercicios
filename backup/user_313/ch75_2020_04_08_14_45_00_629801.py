def eh_primo(x):
    if(x == 0 or x == 1):
        return(False)
    if (x == 2):
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

def verifica_primos(l1):
    dicionario = {}
    for i in l1:
        if eh_primo(i):
            dicionario[i] = True
        else:
            dicionario[i] =  False

           
          
    return dicionario