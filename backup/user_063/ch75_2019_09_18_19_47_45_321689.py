def eh_primo(x):
    y=2
    if x==2 or x==-2:
        return True   
    if x==0 or x==1 or x==-1:
        return False
    while abs(x)>y:        
        if abs(x)%y==0:
            return False        
        else:
            return True
        y+=1
        
def verifica_primos(lista):
    dicionario = {}
    i = 0
    while i < (len(lista)):
        booleano = eh_primo(   lista[i]   )
        dicionario[lista[i]] = booleano
        i += 1
    return dicionario