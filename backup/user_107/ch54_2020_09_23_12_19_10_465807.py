def calcula_fibonacci (length):
    fibo = [1, 1]
    
    while len(fibo) < length:
        fibo_n = fibo[-1] + fibo[-2]
        
        fibo.append(fibo_n)
        
    return fibo