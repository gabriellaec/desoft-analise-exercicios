def calcula_fibonacci(n):
    listaf=[0]*n
    listaf[0]=1
    listaf[1]=1
    for i in range(n):
        listaf[i]=listaf[i-1]+listaf[i-2]
    return listaf