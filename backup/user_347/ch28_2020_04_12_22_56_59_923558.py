i = [0]*90
i[0] = 1
n = 1
while n <= 99:
    n = 1/(2**n)
    i.append(n)
    n = n+1
print(sum(i))
    
    
