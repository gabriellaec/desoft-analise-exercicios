def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 2 !=0:
        i = 3
        while i < x:
            if n % i != 0:
                i = i + 2
            elif n % i == 0: 
                return False
        return True

i = 0
while i < n:
    if eh_primo(i) == True:
        print(i)
        i=i+1
    else:
        i = i + 1