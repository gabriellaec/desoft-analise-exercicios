def primo(n):
    i=2
    if n==2:
        return True
    else:
        while i<n:
            if n%i==0:
                return False
            else:
                i+=1
        return True
    
def maior_primo_menor_que(x):
    if x<2:
        return -1
    elif primo(x)==True:
        return x
    else:
        i = x-1
        while i>0:
            if primo(i)==False:
                i-=1
            else:
                return i
            