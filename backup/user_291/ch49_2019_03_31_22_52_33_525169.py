numeros = []

Vdd = True

while Vdd:
    pos = int(input("numero?: " ))
    if pos > 0:
        numeros.append(pos)
    else:
        Vdd = False
print(numeros[ : :-1])
        