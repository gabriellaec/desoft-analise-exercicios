def eh_primo(k):
    c = 2
    while c<=(k-1):
        if k%c == 0:
            return False
        c+=1
return True

def maior_primo_menor_que(n):
    c = n
    while c>=2:
        if eh_primo(c):
            return c
        c -=1
return -1