def eh_primo(x):
    if x<2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        n = 3
        while n < x:
            if x % n == 0:
                return False
            n += 2
        return True
x = int(input("escreva um número: "))
print (eh_primo(x))