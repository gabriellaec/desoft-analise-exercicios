def eh_primo(num):
    div = 3
    if num == 2:
        True
    elif num == 0:
        False
    elif num % 2 == 0:
        False
    elif num % div == 0:
        False
        while div < num:
            div += 2
    else:
        True