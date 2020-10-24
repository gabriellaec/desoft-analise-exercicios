def eh_primo(x):
    if x==1 or x==0:
        return False
    elif x==2:
        return True
    elif x>1:
        if x%2==0:
            return False 
        else:
            y=3
            invalid=True 
            while invalid:
                if y<x and x%y==0:
                    return False
                elif y==x:
                    return True
                    invalid=False
                y+=2
def lista_primos(n):
    lista=[]
    i=0
    a=0
    while i<n:
        if eh_primo(a):
            lista.append(a)
            i+=1
            a+=1
            lista.sort()
        else:
            a+=1
        return lista