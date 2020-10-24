def eh_primo (k):
    div = 2
    while k % div != 0 and div <= k:   
        div = div + 1
    if k == 0 or k ==1:
        return False
    elif k % div == 0:
        return True
    else:
        return False

            
            
           