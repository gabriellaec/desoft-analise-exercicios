import string
def quantos_uns(x):
    n = 0
    x = string.digits
    while(n<1000):
        if "1" in x:
            n+=1
            return n*1
    
        