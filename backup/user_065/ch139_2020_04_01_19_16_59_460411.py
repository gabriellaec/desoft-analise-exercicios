def arcotangente(x, n):
    result = x
    sqr = 1.0
    negative = 1
    for k in range(n):
        if negative is 0:
            result += (result ** sqr) / sqr

        if negative is 1:
            result -= (result ** sqr) / sqr
            negative = 0
        
        sqr += 2.0
        n += 1
    return result
        
            
        