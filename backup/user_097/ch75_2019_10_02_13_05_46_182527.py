def eh_primo(n):
    primo = True
    if(n%2==0 and n!=2) or (n==1) or (n < 0):
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

def verifica_primos(lista_numeros):
    dic_primos = {}
    i = 0
    while (i < len(lista_numeros)):
        if(eh_primo(lista_numeros[i])==True):
            dic_primos[lista_numeros[i]] = True
            i = i + 1
        else:
            dic_primos[lista_numeros[i]] = False
            i = i + 1
    return dic_primos