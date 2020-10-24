n = 1
while n <= 1000:
    a = n
    s = 1
    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        s += 1
        
    if n == 1:
        tam = s
        num = n
    elif s >= tam:
        tam = s
        num = n
    n += 1
print(num)