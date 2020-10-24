def eh_primo(x):
    if x == 2:
        return True
    elif x == 1 or x == 0:
        return False
    y=3
    while x>2:
        if x%2 == 0:
            return False
        elif x == y:
            return True
        elif x>y and x%y == 0:           
            return False            
        else:
            y+=2
            return True
def lista_primos(n):
    lista=[]
    a=0
    while len(lista)<=n-1:
        if eh_primo(a):
            lista.append(a)
            a+=1           
            lista.sort()
        else:
            a+=1   
    print (lista)
    return lista
  