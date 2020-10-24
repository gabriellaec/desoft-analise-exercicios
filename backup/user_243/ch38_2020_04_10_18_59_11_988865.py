def  quantos_uns(num):
    i=0
    n=0
    num=str(num)
    while i<len(num)-1:
        if num[i]=="1":
            n+=1
            i+=1
    return n