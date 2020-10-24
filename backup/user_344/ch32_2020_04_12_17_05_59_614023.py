def eh_primo(numero):
    if numero == 2:
        return True
    elif numero < 2:
        return False
    elif numero % 2 == 0:
        return False
    n = 3 
    while n< numero:
        if numero % n == 0:
            return False
        n+=2
    return True



def lista_primos(n):
    lista = [0]*n
    i=0
    Lista_certa = []
    a=1
    while i<len(lista):
        lista[i]= a   
        if eh_primo(lista[i])== True:
            Lista_certa.append(lista[i])
    
    a+=1
    i+=1
    return Lista_certa