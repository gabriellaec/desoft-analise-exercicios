ini = float(input())
men = float(input())
taxa = float(input())

total = ini
juros = 0

for c in range(24):
    total += total*(taxa/100)
    juros += total*taxa
    total += men
    print("{:.2f}".format(total))
    
print("{:.2f}".format(juros))
