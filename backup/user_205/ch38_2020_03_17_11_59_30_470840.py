def quantos_uns(x):
    n = 0
    x_str=str(x)
    while(n<x):
        if "1" in x_str[0:12]:
            n+=1
            return n
        else: 
            return None
       
    

        