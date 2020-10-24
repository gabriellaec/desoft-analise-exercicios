
def quantos_uns(x):
    n = 0
    x_str=str(x)
    while(n<x):
        if "1" in str(x):
            n+=1
            return n*1
    
        