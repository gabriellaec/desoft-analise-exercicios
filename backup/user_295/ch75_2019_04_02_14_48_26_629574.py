def verifica_primos (lista):
    i = 2
    dic = {}
    for num in lista:
        i=2
        while i < num:
            if num % i == 0:
                dic[num]=False
            i += 1
        if num not in dic:
            dic[num]=True
    return dic        
                 