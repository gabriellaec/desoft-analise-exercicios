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
        
def lista_primos(n):      
    i = 0
    j = []
    while i<n:
        z = eh_primo(i)
        if z == True:
            j.append(i)
        i+=1
    return j
        
    