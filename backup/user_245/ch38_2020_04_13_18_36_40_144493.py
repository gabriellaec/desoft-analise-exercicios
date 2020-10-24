def quantos_uns(num):
    n = 0
    for i in range(len(num)):
        if num[i] == 1:
            n+=1
    return n
            