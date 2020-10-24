def eh_Primo (k):
    div = 2
    while k % div != 0 and div <= k:   
        div = div + 1
    if k % div == 0:
        return True
    else:
        return False
print (eh_Primo(23))
            
            
           