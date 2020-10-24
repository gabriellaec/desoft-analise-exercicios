def eh_primo (n):
    if n==0 or n==1:
        return False
    if n==2:
        return True
    if n==3:
        return True
    if n==5:
        return True
    else:
        if n%2==0:
            return False
        else:
            i = 3
            while i<n:
                if n%i ==0:
                    return False
                else:
                    i+=2
            return True 

def lista_primos (n):
    lista = []
    i=0
    while len(lista)<n:
        if eh_primo(i)==True:
            lista.append(i)
        i+=1
    return lista