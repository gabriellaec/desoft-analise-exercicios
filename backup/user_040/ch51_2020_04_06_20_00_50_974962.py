def eh_primo(x):
    y = 3
    if (x%2==0 and x!=2 or x==1 or x==0):
        return False
    
    while x>y:
        if x%y==0:
            return False
        y+=2
    return True

def primos_entre(a,b):
    lista = []
    p = a
    while p < b:
        if eh_primo(p) == True and p > 0:
            lista.append(p)
            p +=1
        elif p < 0:
            p +=1
        else:
            p +=1
    return lista