
def verifica_primos (lista):
    i = 2
    dic = {}
    for num in lista:
        i=2
        while i < num:
            if num % i == 0:
                dic[num]=False
            i += 1
        if num == 1:
            dic [num] = False
        elif num not in dic:
            dic[num]=True
    return dic        
                 

print (verifica_primos([1,2,3,4,5,6,7,8,9,10,11,12,13]))
                 