def calcula_fibonacci(n):
    listaf=[]
    listaf[0]=1
    listaf[1]=1
    for i in range(0,n):
        listaf[i]=listaf[i-1]+listaf[i-2]
    return listaf