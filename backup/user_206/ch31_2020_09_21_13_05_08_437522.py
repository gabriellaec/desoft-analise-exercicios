def eh_primo(num):
    if num % 2 == 0:
        False
    div = 3
    while div < num:
        div += 2
    elif num % div == 0:
        False
    else:
        True