n = 999 #numero positivo menor que 1000
sequencia = []
while n > 1:
    i = n
    sequencia_collatz = [i]
    while i > 1:
        if i % 2 == 0:
            i = i/2
            sequencia_collatz.append(i)
        else:
            i = 3*i + 1
            sequencia_collatz.append(i)
    sequencia.append(sequencia_collatz)
    n-=1
x = 0
maior = []
for m in sequencia:
    m = len(sequencia[x])
    maior.append(m)
    x+=1

maior_sequencia = max(maior)
print (maior_sequencia)
n_maior_sequencia = maior.index(maior_sequencia)
print (999 - n_maior_sequencia)