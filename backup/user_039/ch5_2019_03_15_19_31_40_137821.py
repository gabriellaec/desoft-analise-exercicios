def primo(n):
    i=2
    while i<n:
        if n%i==0:
            return False 
        else:
            i+=1
    return True
def maior_primo_menor_que(x):
    i=x-1
    if x<=2:
        return -1
    else:
        while i>0:
            if primo(i)==False:
                i-=1
            else:
                return i
            