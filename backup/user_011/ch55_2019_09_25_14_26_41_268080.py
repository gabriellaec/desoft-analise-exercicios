def eh_primo(n):
    primo = True
    a = 2
    if n == 0 or n == 1:
        return False
    while a<n:
        if n%a == 0:
            return False
        a+=1        
    return True

def primos_entre(a,b):
    lista_p = []
    i = a
    while i <= b:
        if eh_primo(i) == True:
            lista_p.append(i)
    return lista_p