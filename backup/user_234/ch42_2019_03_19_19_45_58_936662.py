def quantos_uns(num):
    contador = 0
    i = 0
    len_num = len(num)
    
    while i < len_num:
        if num[i] == "1":
            contador += 1
        i+=1
    return contador