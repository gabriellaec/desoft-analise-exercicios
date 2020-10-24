def lista_collatz(n):
    lista = [n]
    num = n
    while num != 1:
        if num%2==0:
            num = int(num/2)
        else:
            num = int(3*num + 1)
        lista.append(num)
    return lista

len_max = 0
idx_max = 0
for i in range(1,1000):
    print(i)
    len_collatz = len(lista_collatz(i))
    if len_collatz > len_max:
        len_max = len_collatz
        idx_max = i

print(idx_max, len_max)
