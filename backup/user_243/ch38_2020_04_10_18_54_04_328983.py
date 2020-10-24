def  quantos_uns(num):
    i=0
    n=0
    num=str(num)
    while i<len(num):
        if num[i]==i:
            n+=1
    return n