def eh_primo(x):
    y=2

    if x==2:
        return True    
    if x<2:
        return False
    while x>y:        
        if x%y==0:
            return False        
        y+=1
    return True
        
def verifica_primos(lista):
    dicionario = {}
    i = 0
    while i < (len(lista)):
        booleano = eh_primo(   lista[i]   )
        dicionario[lista[i]] = booleano
        i += 1
    return dicionario
a = verifica_primos([-1,0,1,2,3,4,5,6,7,8,9])
print (a)