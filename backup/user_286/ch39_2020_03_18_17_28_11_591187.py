def par(n):
    n = n/2
    return n

def impar(n):
    n = 3*n + 1
    return n

def collatz(n):
    lista = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(par(n))
            lista.append(n)
        else:
            n = int(impar(n))
            lista.append(n)
    return lista

limite = 999
lista = []
while limite != 0:
    lista.append(len(collatz(limite)))
    limite -= 1

max = lista.index(max(lista))

print (999 - max)
