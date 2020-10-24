def eh_primo(x):
    if x <= 1:
        return False
    else:
        if x%2 == 0:
            return False
        else:
            if x%2 and x%3:
                return False
            else:
                return True