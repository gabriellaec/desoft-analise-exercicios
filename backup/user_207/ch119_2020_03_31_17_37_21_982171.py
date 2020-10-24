def fatorial (y):
    count =1
    fatorial = 1
    while count <= y:
        fatorial *= count
        count += 1
    return fatorial

def calcula_euler (x,n):
    i =0
    euler = 0
    while i<n:
        euler += x**i / fatorial(i)
    return euler


