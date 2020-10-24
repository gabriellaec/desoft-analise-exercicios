def calcula_fibonacci(n):
    list = []
    i=1
    while i < n:
        list.append(i-1+i)
        i=i+1
    return list