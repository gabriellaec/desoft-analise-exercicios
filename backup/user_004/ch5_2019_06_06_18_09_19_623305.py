def primo(n):
    if n%n==0 and n%1==0 and n%2==0:
        return False
    elif n%n==0 and n%1==0 and n%5==0:
        return False
    elif n%n==0 and n%1==0 and n%3==0:
        return False
    else:
        return True

def maior_primo_menor_que(n):
    a = False
    if primo(n) == True:
        return n
    else:
        while a != True:
            n-=1
            if primo(n) == True:
                a = True
        return n

print(maior_primo_menor_que(90))