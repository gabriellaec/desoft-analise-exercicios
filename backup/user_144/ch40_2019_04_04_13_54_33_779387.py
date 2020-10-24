def fatorial(n):
    fact = 1 
    termo = 0
    i = 0
    while i < n:
        termo = n - i
        fact *= termo
        
    return fact

        