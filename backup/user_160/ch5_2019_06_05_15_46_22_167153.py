def maior_primo_menor_que (n):
    i = 0
    if n - i < 2 or n - i % 2 == 0 or n - i % 3 == 0:
        return -1
    elif n - i > 2 and n - i % 2 != 0 and n - i % 3 != 0:
        return n
    else:
        i += 1  
        
        
    