n = 999
sequencias = []
while n > 1:
    sequencia_collatz = [n]
    if n % 2 == 0:
        n = n/2
        sequencia_collatz.append(n)
    else:
        n = ((n*3) + 1)
        sequencia_collatz.append(n)
    sequencias.append(sequencia_collatz)
    n -= 1

x = 0
maior = []
for m in sequencias:
    m = len(sequencias[x])
    maior.append(m)
    x += 1
maior_sequencia = max(maior)
print(maior_sequencia)
n_maior_sequencia = maior.index(maior_sequencia)
print(999 - n_maior_sequencia)