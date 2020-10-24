def fatorial(n):
    if n<0:
        return False
    else:
        total = 1
        i = 2
        while i<=n:
            total *= i
             i-=1
        return total
        
        