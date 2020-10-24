max_lista = 0 
n = 0

for i in range(2,1000):
    lis = [i]
    while lis[-1] != 1:
        if lis[-1]%2==0:
            lis.append(lis[-1]/2)
        else:
            lis.append(lis[-1]*3 + 1)
    if len(lis)>max_lista:
        max_lista = len(lis)
        num = i
print(max_lista + 1)
print(num)
        