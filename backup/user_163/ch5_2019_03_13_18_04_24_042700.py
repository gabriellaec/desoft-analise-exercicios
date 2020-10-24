def is_primo(num):

    i = 2
    check = 0

    while(i<num):

        check += num % i

    if(check == 0):

        return(1)

    return(0)

def maior_primo_menor_que(num):

    i = 0
    low = 0

    while(i < num):

        if(is_primo(num) == 1):

            low = num

    return num
