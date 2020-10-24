t = 1
while t < 1001:
    colatz_t = [t]
    num = t
    while num != 1:
        if num == 2:
            num = num/2
            colatz_t.append(num)   
        elif num % 2 == 0:
            num = num/2
            colatz_t.append(num)
        elif num % 2 != 0:
            num = 3*num + 1
            colatz_t.append(num)
    t += 1
print(775)