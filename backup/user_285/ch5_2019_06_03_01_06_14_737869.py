def verifica_primo(n):
    if n<0:
        return -1
    num=3
    while num<n:
        if n%2==0 or n%num==0:
            return False
        num+=2
    if n==0 or n==1:
        return False
    
    else:
        return True
def maior_primo_menor_que(n):
    if verifica_primo(n)== True:
        return n
    elif verifica_primo(n)== False:
        lista=[]
        for e in range(n):
            if verifica_primo(n-e)==True:
                return n-e
            else:
                return -1
    else:
        return -1
    