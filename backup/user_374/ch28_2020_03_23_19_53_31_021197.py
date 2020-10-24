n = 0
calcula = 1

while n < 100:
    calcula = calcula + (1/(2**n))
    n = n + 1
    
    if n == 99:
        print(calcula)
