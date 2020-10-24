i = 1
lista = []
while i<999:
    c = 0
    n = i
    while True:
        if n % 2 == 0:
            n = n/2
            c += 1
        elif n==1:
            lista.append(c)
            break
        else:
            n = n*3+1
            c +=1
    i += 1
print(lista.index(max(lista))+1)   