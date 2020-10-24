def eh_primo(i):
    j=1
    c=0
    while(j<i):
        if(i%j==0):
            c+=1
        j+=1
    
    if(c != 1):
        return False
    else:
        return True

def verifica_primos(lista):
    dic={}
    
    for i in lista:
        dic[i]=eh_primo(i)
    
    return dic