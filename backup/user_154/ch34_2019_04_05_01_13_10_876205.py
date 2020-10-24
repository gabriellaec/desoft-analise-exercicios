inicial = float(input("Start"))
taxa = float(input("Taxa"))
final = inicial

i = 0

while i < 24:
    print("{0:.2f}".format(final*taxa))
    final = final*(1+taxa)
    i = i + 1

print("{0:.2f}".format(final - inicial))