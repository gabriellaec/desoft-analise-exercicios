lista = []
n = 1000
while n != 1:
    if n % 2 == 0:
        n += n/2
        lista.append(n)
    else:
        n += 3*n + 1
        lista.append(n)
print (len(lista))