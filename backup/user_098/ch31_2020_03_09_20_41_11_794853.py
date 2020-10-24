def eh_primo(num):
    if num == 0 or num == 1:
        return True
    else:
        if num == 2:
            True
        elif num%2 == 0:
            return False
        else:
            x = 3
            while(x < num):
                if num % x == 0:
                    break
                x = x + 2
            if x == num:
                return True
            else:
                return False