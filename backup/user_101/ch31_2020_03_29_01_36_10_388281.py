def eh_primo(num):
    if num == 2:
        return True
    else:
        if num % 2 == 0 or num == 0 or num == 1:
            return False
        else:
            divisor = 1
            while divisor <= num:
				divisor += 2
                if num % divisor != 0:
                    return True
                else:
                    return False
