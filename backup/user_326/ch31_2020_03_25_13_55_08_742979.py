def eh_primo(num):
    if num == 1 or num == 0:
        return False
    elif num == 2:
        return True
    else:
        if num % 2 == 0:
            return False
        else:
            x = 3
            while x < num:
                if num % x == 0:
                    break
                x += 2
            if x == num:
                return True
            else:
                return False
