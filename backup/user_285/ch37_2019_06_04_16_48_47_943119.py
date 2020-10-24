def eh_primo(num):
    n=3
    while n<num:
        if num%2==0 or num%n==0:
            return False
        n+=2
    if num==0 or num==1:
        return False
    
    else:
        return True
    
def lista_primos(n):
    lista_cre=[]
    i=0
    while len(lista_cre)<n:
        if eh_primo(i):
            lista_cre.append(i)
        i+=1
    return lista_cre
            
            