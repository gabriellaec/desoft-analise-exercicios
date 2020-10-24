def zera_negativos(n):

    pos = 0

    for num in n:

        if num < 0:

            n[pos] = 0

            pos+=1

        else:
            pos+=1

    return(n)