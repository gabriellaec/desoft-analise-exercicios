def calcula_fibonacci(n):
    listaf=[0]*n
    listaf[0]=1
    if n>1:
        listaf[1]=1
        if n>2:
            i=2
            while i<n:
                listaf[i]=listaf[i-1]+listaf[i-2]
                i+=1
    return listaf