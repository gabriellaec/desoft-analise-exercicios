def maior_primo_menor_que(n):
    if n == 2:
        return True 
    elif n == 0 or n == 1:
        return False 
    elif n%2 == 0 :
        return False 
    i = 3
    while i <= n:
        if i%2 == 0 :
            return false 
        i +=2
    return True