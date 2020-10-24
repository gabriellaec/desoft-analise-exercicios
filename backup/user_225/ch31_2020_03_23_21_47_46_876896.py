def éPrimo (k):
    div = 2
    while k % div != 0 and div <= k:   
        div = div + 1
        if k % div == 0:
            k = k - 1
        else:
            print (k)