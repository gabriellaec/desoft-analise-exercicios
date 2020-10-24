def calcula_fibonacci(n):
    list = []
    i=1
    while i < n:
        f= (i-1) + i
        list.append(f)
        i=i+1
    return list