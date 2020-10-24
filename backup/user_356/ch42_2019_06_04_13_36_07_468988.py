def quantos_uns(num):
    s=0
    for i in range(len(num)):
        if num[i]=='1':
            s+=1
    return s