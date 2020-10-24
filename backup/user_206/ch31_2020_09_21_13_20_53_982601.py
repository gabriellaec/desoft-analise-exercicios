def eh_primo(num):
    div = 3
    if num == 2:
        print(True)
    elif num == 0 | num == 1:
        print(False)
    elif num % 2 == 0:
        print(False)
    elif num % div == 0:
        print(False)
        while div < num:
            div += 2
    else:
        print(True)