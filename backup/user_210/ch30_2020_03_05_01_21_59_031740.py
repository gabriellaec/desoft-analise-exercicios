ini = float(input())
men = float(input())
taxa = float(input())

total = ini
juros = 0

for c in range(24):
    total += total*(1+taxa)
    juros += total*taxa
    print(total)
    total += men
print(juros)

    