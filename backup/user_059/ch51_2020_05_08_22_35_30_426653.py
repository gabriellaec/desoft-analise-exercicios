def eh_primo(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        if x%2==0: 
            return False
        else:
            i = 3
            while i<x:
                if x%i == 0:
                    break
                i+=1
            if i==x:
                return True
            else:
                return False 
            
def primos_entre(a, b):
    i = b
    l = []
    while i>=a:
        w = eh_primo(i)
        if w == True:
            l.append(i)
        i = i-1
    return l