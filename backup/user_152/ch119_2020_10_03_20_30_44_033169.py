def calcula_euler (x, n):
    ex = 1+x
    i = 0
    j = 2
    fat = 1 
    while i < n:
        x = (x**n)
        while j<= n:
            fat = fat*j
            j += 1
        ex += x/fat
        i += 1
    return ex