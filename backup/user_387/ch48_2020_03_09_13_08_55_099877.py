def eh_crescente(a):

    n = 0
    while n < (len(a) - 1):
        if a[n] >= a[n+1]:
            return False

        else:
            n+=1

    return True