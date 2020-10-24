ini = float(input())
men = float(input())
taxa = float(input())

total = ini
juros = 0
print(total)

for c in range(23):
    total += total*(1+taxa)
    juros += total*taxa
    print(total)
    total += men
print(juros)

    