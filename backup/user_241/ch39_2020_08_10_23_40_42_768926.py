n = 999
maiorc = 1
maiornum = 999 
while n > 0:
    cnt = 1
    i = n
    while i != 1:
        if i % 2 == 0:
            i = (i//2)
        elif i % 2 == 1:
            i = (3*i + 1)
        cnt += 1
    if cnt > maiorc:
        maiorc = cnt
        maiornum = n
    n -= 1
print(maiornum)