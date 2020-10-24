def essenumeroai(num):
    num = str(num)
    list_num=list(num)
    lista_numq=[]

    for n in list_num:
        n = int(n)
        lista_numq.append((n**n))
    soma = sum(lista_numq)
    if num == str(soma):
        return True
    else:
        return False

num = 2
print(essenumeroai(num))