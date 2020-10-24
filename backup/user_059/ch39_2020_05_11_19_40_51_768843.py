j = 999
sequencias = []
while j >1:
    i = j
    sequencia_collatz = [i]
    while i > 1:
        if i % 2 == 0:
            i = (i/2)
            sequencia_collatz.append(i)
        else:
            i = ((i*3)+1)
            sequencia_collatz.append(i)
    sequencias.append(sequencia_collatz)
    j = j-1
k = 0
maior = []
for k in sequencias:
    k = len(sequencias[k])
    maior.append(k)
    k+=1
maior_sequencia = max(maior)
print(maior_sequencia)
n_maior_sequencia = maior.index(maior_sequencia)
print(999 - n_maior_sequencia)