ini = float(input())
men = float(input())
taxa = float(input())

total = ini

for c in range(24):
    total += total*(taxa/100)
    total += men
    print("{:.2f}".format(total))
    
print("{:.2f}".format(total-ini))
