def eh_primo(n):
    primo = True
    if(n%2==0 and n!=2) or (n==1):
        primo = False
    i = 2
    while (i<n):
        if(i%2!=0):
            if(n%i==0):
                primo = False
        i = i + 1
    if(primo==True):
        return True
    else:
        return False

def lista_primos(lp):
    i = 0
    lista = []
    while (len(lista)<lp):
        if(eh_primo(i)==True):
            lista.append(i)
        i = i +1
    return lista