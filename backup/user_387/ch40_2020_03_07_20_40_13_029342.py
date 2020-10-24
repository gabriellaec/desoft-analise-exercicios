def soma_valores(a):
    b = 0
    
    for num in a:
         
        num = (num ** 2) ** (1/2)
        b = b + num
        
    return(b)