def quantos_uns(num):
    num=str(num)
    i=0
    count=0
    while i<len(num):
        if num[i] == 1:
            count+=1
            i+=1
            return count
        else:
            i+=1
        