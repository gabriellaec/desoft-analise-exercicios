def eh_primo (n):
    if n==0 or n==1:
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

def maior_primo_menor_que (n):
    if eh_primo(n) == True:
        return n
    else:
        i = 0
        while i<n:
            i+=1
            if eh_primo(n-i)==True:
                return n-i
        return -1 
            