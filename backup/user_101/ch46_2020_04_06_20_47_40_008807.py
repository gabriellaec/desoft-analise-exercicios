def numero_no_indice(l):
    li = []
    for i, num in enumerate(l):
        if i != num:
            del(num)
    return li

lili = [0, 1, 3, 5, 4]
print (numero_no_indice(lili))
