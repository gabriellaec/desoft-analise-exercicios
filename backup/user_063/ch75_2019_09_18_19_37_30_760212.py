def eh_primo(x):
    y=2

    if x==2:
        return('Ã primo')
    
    if x==0 or x==1:
        return ('NÃ£o Ã© primo')
    while x>y:        
        if x%y==0:
            return ('NÃ£o Ã© primo')
        
        else:
            return ('Ã primo')
        y+=1
        
def verifica_primos(lista):
    dicionario = {}
    i = 0
    while i < (len(lista)):
        booleano = eh_primo(   lista[i]   )
        dicionario[lista[i]] = booleano
        i += 1
    return dicionario