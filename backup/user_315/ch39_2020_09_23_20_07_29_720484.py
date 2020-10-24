def sequencia(n):
    if n == 1 or n == 0:
        return 1

    elif n%2 == 0:
        y = n/2
        return y
        
    elif n%2 != 0:
        y = 3*n+1
        return y

n=1
s=0

while n < 1000:
    temp = n
    i = 0
    while temp != 1:
        temp = sequencia(temp)
        i += 1
        if s < i:
            s = i
            w = n
            n += 1

 print (w)