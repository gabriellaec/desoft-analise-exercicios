def quantos_uns(num):
    s=0
    b=len(num)
    for i in range(b):
        if num[i]=='1':
            s+=1
    return s