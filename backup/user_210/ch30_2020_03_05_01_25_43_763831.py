ini = float(input())
men = float(input())
taxa = float(input())

total = ini
juros = 0

for c in range(24):
    total += total*(taxa)
    juros += total*taxa
    total += men
    print(total)
    
print(juros)