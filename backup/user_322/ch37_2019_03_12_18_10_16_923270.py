def eh_primo(x):
    if x < 2:
        return False
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    elif x % 2 !=0:
        i = 3
        while i < x:
            if x % i != 0:
                i = i + 2
            elif x % i == 0: 
                return False
        return True

i = 0
while i < n:
    if eh_primo(i) == True:
        print(i)
        i=i+1
    else:
        i = i + 1