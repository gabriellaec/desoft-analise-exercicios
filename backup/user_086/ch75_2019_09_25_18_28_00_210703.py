def eh_primo(numero):
    impar=3
    if numero==0 or numero==1:
        return False
    if numero==2:
        return True
    if numero%2==0:
        return False
    while impar<numero:
        if numero%impar==0:
            return False
        impar+=2
    return True

def verifica_primos(listanum):
    dicionario=dict()
    i=0
    while i<len(listanum):
        numero=eh_primo(listanum[i])
        if numero==True:
            dicionario[listanum[i]]=True
        else:
            dicionario[listanum[i]]=False
    return dicionario
    
    
    
    
    