def eh_primo(n):
    div=3
    if n%2==0 and n!=2 or n==1 or n==0:
        return False
    while n > div:
        if n%div==0:
            return False
        div +=2
    return True

def maior_primo_menor_que(n):
    lista=[]
    for i in range(0, n+1):
        if eh_primo(i):
            lista.append(i)
    if n<=0 or n==1:
        return -1
    return lista[-1]