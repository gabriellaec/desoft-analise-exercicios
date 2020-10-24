def eh_primo (n):
    if n<=1:
        return False
    if n==2:
        return True
    if n==3:
        return True
    if n==5:
        return True
    else:
        if n%2==0:
            return False
        else:
            i = 3
            while i<n:
                if n%i ==0:
                    return False
                else:
                    i+=2
            return True

def primos_entre (a,b):
    i = 0 
    lista=[]
    while i < b-a+1:
        if eh_primo(a+i) == True:
            lista.append(a+i)
        i+=1
    return lista