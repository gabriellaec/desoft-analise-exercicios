a = 0
n = 0
i = 5
b = i
while i<1000:
    x = 1
    while i!=1:
        if i%2==0:
            i = i/2
        else:
            i = 3*i+1
        x += 1
    if x >= a:
        a = x
        n = b
        i = b+1
        b = i
    else:
        i = b+1
        b = i
print(n)