def maior_primo_menor_que(n):
    if n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(4,n):
            if i% 2 != 0 and i%3 != 0:
                return True
            
            
        
    