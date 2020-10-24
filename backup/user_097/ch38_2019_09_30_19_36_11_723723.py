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
    i = a
    contador = 0
    while(i>=a and i<=b):
        if(eh_primo(i)==True):
            contador = contador + 1
        i = i + 1
    return contador

print(primos_entre(19, 41))