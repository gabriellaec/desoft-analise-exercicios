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
lista2 = []
def primos_entre(a, b):
    j = a
    while a<j<b:
        if eh_primo(a+j):
            lista2.append(a+j)
        j+=1
    return lista2