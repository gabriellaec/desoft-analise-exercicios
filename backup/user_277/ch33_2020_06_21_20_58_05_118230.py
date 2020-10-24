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

def primos_entre(a, b):
    lista = []
    k = a
    while a <= k <= b:
        if eh_primo:
            lista.append(k)
        k+=1
    return len(lista)
    