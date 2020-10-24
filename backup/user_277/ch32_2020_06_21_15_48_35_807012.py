def eh_primo(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    for i in range(3,n,2):
        if n%2==0:
            return False
        elif n%i==0:
            return False
    return True

lista = []

def lista_primos(n):
    if eh_primo(n) == True:
        lista.append(n)
    return lista
