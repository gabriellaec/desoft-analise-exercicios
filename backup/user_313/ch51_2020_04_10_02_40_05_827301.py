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

lista = []
cont = 0
def primos_entre(a,b):
    
    cont = a
    while cont <= b:
        
        if eh_primo(cont) == True:
            lista.append(cont)
            cont += 1
        
        else:
            cont += 1

    return(lista)