x = 999
collatz = []
while x > 1:
    i = x 
    sequencia_collatz = [i]
    while i > 1:
        if i % 2 == 0:
            i = (i/2)
            sequencia_collatz.append(i)
        else:
            i = ((i*3) +1)
            sequencia_collatz.append(i)
    collatz.append(sequencia_collatz)
    n -=1
y = 0
maior = []
for x in collatz:
    x = len(collatz[y])
    maior.append(n)
    y+=1
maior_sequencia = max(maior)
print(maior_sequencia)
ms = maior.index(maior_sequencia)
print(999 - ms)
