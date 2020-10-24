import math
def arcotangente(x, n):
    result = float(x)
    sqr = 3.0
    negative = 1
    for k in range(n):
        if negative is 0:
            result += (math.pow(result, sqr)/sqr

        if negative is 1:
            result -= (math.pow(result, sqr)/sqr
            negative = 0
        
        sqr += 2.0
        n += 1
    return result
        
            
        