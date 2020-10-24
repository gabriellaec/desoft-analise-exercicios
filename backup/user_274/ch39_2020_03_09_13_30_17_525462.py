i=1

while i < 1000:
    c=0
    while j >= 1:
        if i % 2 == 0:
            j= i/2
            c=c+1
        else:
            j=i*3+1
            c=c+1
    if c > f:
        f=c
        n=i
    i=i+1
    
print(n)