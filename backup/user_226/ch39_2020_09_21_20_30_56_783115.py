numeros = range(1, 999)

def calcula_sequencia(n):
    lista = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            lista.append(n)
        else:
            n = 3 * n + 1
            lista.append(n)
    return lista

i = 1
while i < 1000:
    lista = []
    if len(calcula_sequencia(i)) > len(calcula_sequencia(i - 1)):
        lista.append(i)
    i += 1

print(lista[len(lista) - 1])
