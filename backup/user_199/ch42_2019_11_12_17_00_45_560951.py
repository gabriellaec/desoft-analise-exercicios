def quantos_uns(n):
    s=0
    num=str(n)
    for i in num:
        if i=='1':
            s+=1
    return s
print(quantos_uns(121))