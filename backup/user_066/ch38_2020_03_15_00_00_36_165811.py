def quantos_uns(x):
    k = 0 #quantidade de uns em x
    if x == 1:
        k+=1
    else:  
        while x > 0:
            if x%10 == 0:
                x /= 10
            elif (x-1)%10==0:
                x = (x-1)/10
                k += 1
            else:
                while x%10 != 0 and x>0:
                    x -= 1
    return k