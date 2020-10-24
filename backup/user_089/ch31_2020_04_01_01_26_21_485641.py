def eh_primo(num):
    i = 1
    if num == 0:
        return "False"
    if num == 1:
        return "False"
    if num == 2:
        return "True"
    while i < num:
        if num%i !=  0:
            i = i + 2
        if num%i == 0:
            return"False"
            