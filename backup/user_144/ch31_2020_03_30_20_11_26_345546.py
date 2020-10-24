def eh_primo(primo):
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                return False
            else:
                return False