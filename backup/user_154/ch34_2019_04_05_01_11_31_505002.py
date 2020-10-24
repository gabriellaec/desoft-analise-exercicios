inicial = float(input("Start"))
taxa = float(input("Taxa"))/100
final = inicial

i = 0

while i < 24:
    final = final*(1+taxa)
    print("{0:.2f}".format(final))
    i = i + 1

print("{0:.2f}".format(final - inicial))