def seq(n):
    lista = [n]
    while n != 1 :
        if n % 2 == 0:
            n = n/2
            lista.append(n)
        else:
            n = 3*n + 1
            lista.append(n)
    return lista
t = 0
q = 1
k = 0
while t < 1000:
    if len(seq(t)) > q :
        q = len(seq(t))
        k = t
    t += 1
print(k)

     