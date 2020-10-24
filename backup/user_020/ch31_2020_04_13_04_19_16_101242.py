def eh_primo(num):
    impar = 3
    if num % 2 == 0:
        if num!= 2:
            return False
        else:
            return True
    elif num == 1:
        return False
    else:
        while impar<num:
             if num%impar==0:
                return False
             else:
                impar+=2
             return True