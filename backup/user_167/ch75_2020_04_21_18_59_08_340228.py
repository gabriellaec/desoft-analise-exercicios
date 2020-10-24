def eh_primo(numero):
    if numero==2:
        return False
    elif numero <2:
        return False
    elif %2 ==0:
        return False
    n=3
    while n < numero:
        if numero % n == 0:
            return False
        n+=2
    return True
    




def verifica_primos (lista):
    dic={}
    for e in lista:
        dic[e]= eh_primo(e)
    return dic 
    
    