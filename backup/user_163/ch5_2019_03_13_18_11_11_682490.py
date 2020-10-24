def is_primo(num):

    i = 2
    check = 0

    while(i < num):

        check = (num % i) + check
        i = i + 1

    if(check == 0):

        return(1)

    return(0)

def maior_primo_menor_que(num):

    if(num <= 0):

        return(-1)

    i = 1
    low = 0

    while(i < num):

        if(is_primo(i) == 1):

            low = i

        i = i + 1

    return(low)
