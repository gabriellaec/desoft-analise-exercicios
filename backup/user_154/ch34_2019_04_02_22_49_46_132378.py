inicial = float(input("Start"))
taxa = float(input("Taxa"))/100
final = inicial

i = 0

while i < 24:
    print(final*taxa)
    final = final*(1+taxa)
    i = i + 1

print(final - inicial)