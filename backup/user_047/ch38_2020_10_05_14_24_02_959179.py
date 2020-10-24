def quantos_uns(x):
    count = 0
    uns = 0
    z = str(x)
    while count<len(z):
        if z[count]=='1':
            uns+=1
        count+=1
    return uns