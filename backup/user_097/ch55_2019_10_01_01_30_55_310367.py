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

def primos_entre(a, b):
    lista_primos = []
    if(a>b):
        while(b<=a):
            if(eh_primo(b)==True):
                lista_primos.append(b)
            b = b +1
        return lista_primos
    elif(b>a):
        while(a<=b):
            if(eh_primo(b)==True):
                lista_primos.append(b)
            b = b - 1
        lista_primos = lista_primos[:: -1]
        return lista_primos