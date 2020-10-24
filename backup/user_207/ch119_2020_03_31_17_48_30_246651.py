def calcula_euler (x,n):
    i =1
    euler = 1
    den =1
    
    while i<n:
        den *= i
        euler += x**i / den
        i+=1
    return euler

print (calcula_euler(1,8))


