def eh_primo(n):
    if n==0:
        return False
    elif n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i<n:
            if n%i==0:
                return False
            i+=2
        return True


def verifica_primos(lista):
    verificador={}
    for i in lista:
        booll=eh_primo(i)
        verificador[i]=booll
    return verificador