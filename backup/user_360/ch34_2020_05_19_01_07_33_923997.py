def eh_primo(n):
     if n<2:
            return False 
        elif n==2:
            return True 
        elif n%2==0:
            return False
          else:
        m=3
        while m<n:
            if n%m==0:
                return False
            m+=2
        return True
def maior_primo_menor_que(n):
    i = n
    nenhum = -1
    while i>0:
        w = eh_primo(i)
        if w == True:
            return i
        i = i-1
    return nenhum
